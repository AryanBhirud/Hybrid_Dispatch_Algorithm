from data.grid_data import create_grid as create_grid_data
from src.models import Generator, Storage, Consumer

def create_grid():
    grid_data = create_grid_data()
    return {
        'generators': grid_data['generators'],
        'storage': grid_data['storage'],
        'consumers': grid_data['consumers']
    }