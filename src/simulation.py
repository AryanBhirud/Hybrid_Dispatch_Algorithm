from src.dispatch import hybrid_dispatch
from collections import defaultdict
import numpy as np

HOURS = 24

def run_simulation(grid):
    metrics = defaultdict(list)
    
    for hour in range(HOURS):
        energy_sources, total_generated = hybrid_dispatch(grid, hour)
        
        # Calculate metrics
        total_demand = sum(c.hourly_demand[hour] for c in grid['consumers'])
        metrics['unmet_demand'].append(total_demand - total_generated)
        metrics['total_cost'].append(sum(amt * gen.cost for (src, gen, amt) in energy_sources if src == 'generator'))
        metrics['co2_emissions'].append(sum(amt * gen.co2 for (src, gen, amt) in energy_sources if src == 'generator'))
        metrics['storage_soc'].append(np.mean([s.current_charge/s.capacity for s in grid['storage']]))
        metrics['renewable_usage'].append(
            sum(amt for (src, gen, amt) in energy_sources if src == 'generator' and gen.type in ['Solar', 'Wind', 'Hydro']) / 
            total_generated * 100 if total_generated > 0 else 0
        )
    
    return metrics