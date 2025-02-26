class Generator:
    def __init__(self, name, g_type, max_cap, cost, co2, hourly_production):
        self.name = name
        self.type = g_type
        self.max_cap = max_cap
        self.cost = cost
        self.co2 = co2
        self.hourly_production = hourly_production

class Storage:
    def __init__(self, name, capacity, efficiency, max_discharge):
        self.name = name
        self.capacity = capacity
        self.efficiency = efficiency
        self.max_discharge = max_discharge
        self.current_charge = capacity * 0.5

class Consumer:
    def __init__(self, name, priority, hourly_demand):
        self.name = name
        self.priority = priority
        self.hourly_demand = hourly_demand
        self.hourly_allocation = [0] * 24