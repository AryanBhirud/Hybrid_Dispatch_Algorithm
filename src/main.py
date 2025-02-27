from .grid import create_grid
from .simulation import run_simulation
from .visualize import generate_reports

def main():
    grid = create_grid()
    hybrid_metrics, brute_force_metrics = run_simulation(grid)
    generate_reports(grid, hybrid_metrics, brute_force_metrics)

if __name__ == "__main__":
    main()