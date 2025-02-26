# 🌆 Hybrid Dispatch Algorithm for Smart Cities

This repository is a digital assignment submission for the course **BCSE316L - Design of Smart Cities**. The project consists of a custom **energy distribution algorithm** for a smart city, optimizing energy dispatch based on cost, emissions, and priority-based consumer allocation.

---

## 🚀 **Project Overview**

This project models a **smart grid** for a city, consisting of:
- **Generators**: Multiple energy sources (Solar, Wind, Gas, Coal, Hydro, Nuclear, Oil).
- **Storage Units**: Batteries to store excess energy.
- **Consumers**: Three priority levels (High, Medium, Low) with varying hourly energy demands.

The system uses a **custom energy dispatch algorithm** to:
1. Optimize energy distribution based on **cost** and **emissions**.
2. Prioritize **renewable energy sources**.
3. Use **storage units** efficiently to balance supply and demand.
4. Allocate energy fairly to consumers based on **priority levels**.

---

## 🛠️ **Features**

### **1. Hybrid Dispatch Algorithm**
- **Dynamic Generator Scoring**: Combines cost, emissions, and renewable priority to rank generators.
- **Smart Storage Intervention**: Uses storage units efficiently to meet demand gaps.
- **Renewable Energy Capture**: Stores excess renewable energy for later use.
- **Priority-Based Allocation**: Ensures high-priority consumers (e.g., hospitals) get energy first.

### **2. Simulation**
- Simulates energy distribution over **24 hours**.
- Tracks key metrics:
  - **Unmet Demand**
  - **Total Cost**
  - **CO2 Emissions**
  - **Storage State of Charge**
  - **Renewable Energy Usage**

### **3. Visualization**
- **Interactive Line Graphs**:
  - Combined metrics dashboard.
  - Priority-level demand vs. allocation comparison.
- **Color-Coded Plots** for better readability.

---

## 🧩 **How It Works**

### **1. Grid Configuration**
- The grid is initialized with:
  - **Generators**: Solar, Wind, Gas, Coal, Hydro, Nuclear, Oil.
  - **Storage Units**: Three batteries with varying capacities and efficiencies.
  - **Consumers**: 20 consumers with random hourly demands and priority levels.

### **2. Hybrid Dispatch Algorithm**
1. **Generator Scoring**: Each generator is scored based on cost, emissions, and renewable status.
2. **Energy Dispatch**:
   - Use generators in order of their scores.
   - Use storage units to fill demand gaps.
   - Store excess renewable energy.
3. **Consumer Allocation**:
   - Allocate energy to consumers based on priority levels.
   - Distribute energy proportionally within each priority group.

### **3. Simulation**
- Runs for **24 hours**.
- Tracks and logs key metrics for analysis.

### **4. Visualization**
- Generates **interactive line graphs** for:
  - Unmet demand, total cost, CO2 emissions, storage state of charge, and renewable usage.
  - Priority-level demand vs. allocation.

---

## 🖥️ **How to Run**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Hybrid_Dispatch_Algorithm.git
   cd Hybrid_Dispatch_Algorithm
   ```

2. **Install Dependancies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Repository**:
    ```bash
    python -m src.main
    ```

## 📄 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
```
Hybrid_Dispatch_Algorithm
Copyright (C) 2024 Aryan Bhirud | Saumya Saanvi | Atulya Sahane

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```


## 👨‍💻 **Developed By**
1. Aryan Bhirud  | 22BCE3064
2. Saumya Saanvi | 22BCE3184
3. Atulya Sahane | 22BCE2941