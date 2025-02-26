import numpy as np
from src.models import Generator, Storage, Consumer

HOURS = 24

def create_grid():
    generators = [
        Generator('G1', 'Solar', 100, 15, 0, [30, 40, 50, 60, 70, 80, 90, 100, 80, 60, 40, 20, 30, 50, 70, 90, 100, 80, 60, 50, 40, 30, 20, 10]),
        Generator('G2', 'Wind', 150, 20, 0, [50] * HOURS),
        Generator('G3', 'Gas', 200, 50, 40, [100] * HOURS),
        Generator('G4', 'Coal', 180, 45, 90, [150] * HOURS),
        Generator('G5', 'Hydro', 120, 25, 0, [80] * HOURS),
        Generator('G6', 'Nuclear', 250, 30, 5, [200] * HOURS),
        Generator('G7', 'Oil', 100, 55, 80, [90] * HOURS)
    ]
    
    storage_units = [
        Storage('S1', 300, 0.85, 80),
        Storage('S2', 250, 0.90, 60),
        Storage('S3', 200, 0.80, 50)
    ]
    
    consumers = [
        Consumer(f'C{i+1}', np.random.choice([1,2,3]), [np.random.randint(20, 150) for _ in range(HOURS)])
        for i in range(20)
    ]
    
    return {
        'generators': generators,
        'storage': storage_units,
        'consumers': consumers
    }