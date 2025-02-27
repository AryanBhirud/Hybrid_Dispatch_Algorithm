import matplotlib.pyplot as plt
import numpy as np

HOURS = 24

def generate_reports(grid, hybrid_metrics, baseline_metrics):
    consumers = grid['consumers']
    
    # Combined metrics visualization
    plt.figure(figsize=(18, 12))
    
    metric_titles = [
        ('unmet_demand', 'Unmet Demand (MW)'),
        ('total_cost', 'Total Cost ($)'),
        ('co2_emissions', 'CO2 Emissions (kg)'),
        ('storage_soc', 'Storage State of Charge (%)'),
        ('renewable_usage', 'Renewable Usage (%)')
    ]
    
    for idx, (metric_key, title) in enumerate(metric_titles, 1):
        plt.subplot(2, 3, idx)
        plt.plot(hybrid_metrics[metric_key], label='Hybrid Dispatch', linestyle='-', color='blue')
        plt.plot(baseline_metrics[metric_key], label='Baseline Algorithm', linestyle='--', color='red')
        plt.title(title)
        plt.xlabel('Hour')
        plt.grid(True)
        plt.legend()
    
    # Priority allocation visualization
    plt.subplot(2, 3, 6)
    priority_data = {1: {'demand': [], 'alloc': []},
                     2: {'demand': [], 'alloc': []},
                     3: {'demand': [], 'alloc': []}}
    
    for hour in range(HOURS):
        for prio in [1, 2, 3]:
            p_consumers = [c for c in consumers if c.priority == prio]
            if p_consumers:
                priority_data[prio]['demand'].append(np.mean([c.hourly_demand[hour] for c in p_consumers]))
                priority_data[prio]['alloc'].append(np.mean([c.hourly_allocation[hour] for c in p_consumers]))
    
    for prio in [1, 2, 3]:
        plt.plot(priority_data[prio]['demand'], label=f'Prio {prio} Allocation', linestyle='-')
        plt.plot(priority_data[prio]['alloc'], label=f'Prio {prio} Demand', linestyle='--')
    
    plt.title('Priority Level Demand vs Allocation')
    plt.xlabel('Hour')
    plt.ylabel('Energy (MW)')
    plt.legend()
    plt.tight_layout()
    plt.show()