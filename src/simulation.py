from src.dispatch import hybrid_dispatch, baseline_dispatch
from collections import defaultdict
import numpy as np

HOURS = 24

def run_simulation(grid):
    hybrid_metrics = defaultdict(list)
    baseline_metrics = defaultdict(list)
    
    # Reset grid for random simulation
    original_grid = {
        'generators': [gen for gen in grid['generators']],
        'storage': [store for store in grid['storage']],
        'consumers': [con for con in grid['consumers']]
    }
    
    for hour in range(HOURS):
        # Run hybrid dispatch
        energy_sources, total_generated = hybrid_dispatch(grid, hour)
        total_demand = sum(c.hourly_demand[hour] for c in grid['consumers'])
        hybrid_metrics['unmet_demand'].append(total_demand - total_generated)
        hybrid_metrics['total_cost'].append(sum(amt * gen.cost for (src, gen, amt) in energy_sources if src == 'generator'))
        hybrid_metrics['co2_emissions'].append(sum(amt * gen.co2 for (src, gen, amt) in energy_sources if src == 'generator'))
        hybrid_metrics['storage_soc'].append(np.mean([s.current_charge/s.capacity for s in grid['storage']]))
        hybrid_metrics['renewable_usage'].append(
            sum(amt for (src, gen, amt) in energy_sources if src == 'generator' and gen.type in ['Solar', 'Wind', 'Hydro']) / 
            total_generated * 100 if total_generated > 0 else 0
        )
        
        # Run random dispatch
        energy_sources, total_generated = baseline_dispatch(original_grid, hour)
        total_demand = sum(c.hourly_demand[hour] for c in original_grid['consumers'])
        baseline_metrics['unmet_demand'].append(total_demand - total_generated)
        baseline_metrics['total_cost'].append(sum(amt * gen.cost for (src, gen, amt) in energy_sources if src == 'generator'))
        baseline_metrics['co2_emissions'].append(sum(amt * gen.co2 for (src, gen, amt) in energy_sources if src == 'generator'))
        baseline_metrics['storage_soc'].append(np.mean([s.current_charge/s.capacity for s in original_grid['storage']]))
        baseline_metrics['renewable_usage'].append(
            sum(amt for (src, gen, amt) in energy_sources if src == 'generator' and gen.type in ['Solar', 'Wind', 'Hydro']) / 
            total_generated * 100 if total_generated > 0 else 0
        )
    
    return hybrid_metrics, baseline_metrics