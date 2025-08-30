# Warehouse Picking Route (AI)

This code generate a **warehouse order-picking problem** and compares different routing policies.  
The picker starts at some node, moves on a grid to collect items, and we measure:

- **Total Time** (steps taken)
- **Total Distance** (Manhattan distance traveled)
- **Route** (sequence of coordinates visited)


---

## Type of Routes
- Naive policy (pick the items in given order)
- Greedy policy (pick the items in nearest node)
- TSP policy (pick items in brute-force TSP order)
- Q-learning policy – (pick items using an AI agent that learns the optimal picking order through repeated training)

---

## 📂 Project Structure
```
warehouse-routing/
│── warehouse.py          # distance functions
│── policies.py           # routing policies
│── route_Generator.py    # simulation engine
│── plotting.py           # route plotting
│── main.py               # run example 
```

---

## ▶️ Run the Simulation

```bash
python main.py
```

Example output:
```
Total Time: 10
Total Distance: 10
Route: [(0, 0), (0, 3), (2, 2), (4, 1)]
```

A plot will also open showing the route on the grid.

---
