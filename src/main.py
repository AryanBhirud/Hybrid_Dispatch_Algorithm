from .grid import create_grid
from .simulation import run_simulation
from .visualize import generate_reports

def main():
    grid = create_grid()
    metrics = run_simulation(grid)
    generate_reports(grid, metrics)

if __name__ == "__main__":
    main()