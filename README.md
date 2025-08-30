
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

  

## Project Structure

```

warehouse-routing/

│── warehouse.py # distance functions

│── policies.py # routing policies

│── route_Generator.py # simulation engine

│── plotting.py # route plotting

│── main.py # run example

```

  

---

  

## Run the Simulation

  

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

  

## Q-learning

  

Q-learning is a model-free reinforcement learning algorithm. It learns the best action to take in each state by trial and error.

- State (s) → a description of the environment at a given time.

- Action (a) → what the agent can do in that state.

- Reward (r) → immediate feedback from the environment after taking the action.

- Q-value (Q(s,a)) → expected total reward if you take action a in state s and follow the best strategy afterward.

  

The goal: Learn a Q-table that tells the agent which action is best in any state.

  

***

## Q-learning brief in this warehouse model

***

  
- State (s) → This uniquely describes the “situation” of the picker.

- Action (a) → The next item to pick from the remaining items.

- Reward (r) → Negative distance to next item, because we want to minimize travel. Shorter moves give higher reward.

- Q-value (Q(s,a)) → Learning episodes:

1. Start at first node with all items unpicked.

2. Repeat until all items are picked:

      - Choose next item (action) using epsilon-greedy:

         - With probability ε → explore (pick a random item)

         - With probability 1-ε → exploit (pick best known action from Q-table)

      - Update Q-value for the current state-action pair.

      - Move to next state (picked item removed).

3. Repeat this for many episodes to train the Q-table.


### **After training**

-   Use the Q-table to construct a route:
    
    -   Start at  the starting node
        
    -   Pick the best action (item) from Q-values at each state
        
    -   Continue until all items are picked
