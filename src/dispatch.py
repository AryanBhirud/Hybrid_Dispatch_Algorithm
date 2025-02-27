import numpy as np

def hybrid_dispatch(grid, hour):
    # Calculate dynamic priority score for generators (lower is better)
    def generator_score(gen):
        # Combine cost (60%), CO2 (30%), and renewable priority (10%)
        renewable_bonus = 0.1 if gen.type in ['Solar', 'Wind', 'Hydro'] else 1.0
        return (0.6*gen.cost + 0.3*gen.co2) * renewable_bonus
    
    generators = sorted(grid['generators'], key=generator_score)
    storage_units = grid['storage']
    consumers = sorted(grid['consumers'], key=lambda x: x.priority)
    
    total_demand = sum(c.hourly_demand[hour] for c in consumers)
    energy_sources = []
    storage_used = []
    
    # Phase 1: Generator dispatch with renewable optimization
    remaining_demand = total_demand
    for gen in generators:
        available = min(gen.hourly_production[hour], gen.max_cap)
        used = min(available, remaining_demand)
        energy_sources.append(('generator', gen, used))
        remaining_demand -= used
        if remaining_demand <= 0:
            break
    
    # Phase 2: Smart storage intervention
    if remaining_demand > 0:
        storage_needs = remaining_demand
        for store in sorted(storage_units, key=lambda x: -x.efficiency):
            possible_discharge = min(storage_needs, store.max_discharge, store.current_charge)
            if possible_discharge > 0:
                effective_energy = possible_discharge * store.efficiency
                energy_sources.append(('storage', store, possible_discharge))
                storage_used.append((store, possible_discharge))
                remaining_demand -= effective_energy
                store.current_charge -= possible_discharge
                if remaining_demand <= 0:
                    break
    
    # Phase 3: Renewable energy storage capture
    excess_renewable = sum(
        gen.hourly_production[hour] - sum(amt for src, g, amt in energy_sources if g == gen)
        for gen in generators if gen.type in ['Solar', 'Wind', 'Hydro']
    )
    
    for store in storage_units:
        if excess_renewable <= 0:
            break
        charge_capacity = store.capacity - store.current_charge
        max_charge = min(excess_renewable, charge_capacity / store.efficiency)
        store.current_charge += max_charge * store.efficiency
        excess_renewable -= max_charge
    
    # Phase 4: Priority-based allocation with fairness
    total_available = sum(amt for src, gen, amt in energy_sources if src == 'generator') + \
                     sum(amt * store.efficiency for src, store, amt in energy_sources if src == 'storage')
    
    allocated = 0
    for prio in [1, 2, 3]:
        prio_consumers = [c for c in consumers if c.priority == prio]
        if not prio_consumers:
            continue
        prio_demand = sum(c.hourly_demand[hour] for c in prio_consumers)
        allocation = min(prio_demand, total_available - allocated)
        
        # Distribute allocation proportionally within priority group
        for c in prio_consumers:
            c_share = c.hourly_demand[hour] / prio_demand if prio_demand > 0 else 0
            c.hourly_allocation[hour] = allocation * c_share
        allocated += allocation
    
    return energy_sources, sum(amt for src, gen, amt in energy_sources if src == 'generator') + \
                          sum(amt * store.efficiency for src, store, amt in energy_sources if src == 'storage')
import random

def baseline_dispatch(grid, hour):
    generators = grid['generators']
    storage_units = grid['storage']
    consumers = grid['consumers']
    
    total_demand = sum(c.hourly_demand[hour] for c in consumers)
    energy_sources = []
    
    # Step 1: Randomly select generators and use a random fraction of their capacity
    remaining_demand = total_demand
    random.shuffle(generators)  # Shuffle generators randomly
    
    for gen in generators:
        # Use a random fraction (10-90%) of the generator's capacity
        used = min(gen.hourly_production[hour] * random.uniform(0.1, 0.9), remaining_demand)
        energy_sources.append(('generator', gen, used))
        remaining_demand -= used
        if remaining_demand <= 0:
            break
    
    # Step 2: Randomly use storage units
    if remaining_demand > 0:
        random.shuffle(storage_units)  # Shuffle storage units randomly
        for store in storage_units:
            # Discharge a random fraction (10-90%) of the storage capacity
            discharge = min(remaining_demand * random.uniform(0.1, 0.9), store.max_discharge, store.current_charge)
            energy_sources.append(('storage', store, discharge))
            store.current_charge -= discharge
            remaining_demand -= discharge * store.efficiency
            if remaining_demand <= 0:
                break
    
    # Step 3: Randomly allocate energy to consumers
    total_available = sum(amt for src, gen, amt in energy_sources if src == 'generator') + \
                     sum(amt * store.efficiency for src, store, amt in energy_sources if src == 'storage')
    
    for consumer in consumers:
        # Allocate a random fraction (10-90%) of the available energy
        allocation = total_available * random.uniform(0.1, 0.9)
        consumer.hourly_allocation[hour] = allocation
    
    return energy_sources, sum(amt for src, gen, amt in energy_sources if src == 'generator') + \
                          sum(amt * store.efficiency for src, store, amt in energy_sources if src == 'storage')