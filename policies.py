
import itertools
import random
from warehouse import WarehouseGrid


def naive_rte(order, start):
    return order[:]


def greedy_rte(order, start):
    rte = []
    remaining_items = order[:]
    current = start
    while remaining_items:
        next_node = min(remaining_items, key=lambda p: WarehouseGrid.dist_calc(current, p))
        rte.append(next_node)
        remaining_items.remove(next_node)
        current = next_node
    return rte


def tsp_heur_rte(order, start):
    incumbent_rte = None
    incumbent_dist = float("inf")
    for perm in itertools.permutations(order):
        dist = WarehouseGrid.dist_calc(start, perm[0])
        for i in range(len(perm)-1):
            dist += WarehouseGrid.dist_calc(perm[i], perm[i+1])
        if dist < incumbent_dist:
            incumbent_rte = perm
            incumbent_dist = dist
    return list(incumbent_rte)


# This is the RL AI code
class QLearningAgent:
    def __init__(self, order, start=(0,0), alpha=0.1, gamma=0.9, epsilon=0.2):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.start = start
        self.order = order
        self.Q = {}  # state-action values

    def get_state_key(self, current, remaining_items):
        return (current, tuple(sorted(remaining_items)))

    def choose_action(self, current, remaining_items):
        key = self.get_state_key(current, remaining_items)
        if random.random() < self.epsilon or key not in self.Q:
            return random.choice(remaining_items)
        else:
            return max(self.Q[key], key=self.Q[key].get)

    def update_q(self, state, action, reward, next_state):
        if state not in self.Q:
            self.Q[state] = {}
        if action not in self.Q[state]:
            self.Q[state][action] = 0
        max_next = max(self.Q.get(next_state, {}).values(), default=0)
        self.Q[state][action] += self.alpha * (reward + self.gamma * max_next - self.Q[state][action])

    def learn_episode(self):
        remaining_items = self.order[:]
        current_node = self.start
        rte = [current_node]

        while remaining_items:
            state = self.get_state_key(current_node, remaining_items)
            action = self.choose_action(current_node, remaining_items)
            remaining_next = remaining_items[:]
            remaining_next.remove(action)
            reward = -WarehouseGrid.dist_calc(current_node, action)
            next_state = self.get_state_key(action, remaining_next)
            self.update_q(state, action, reward, next_state)
            current_node = action
            remaining_items = remaining_next
            rte.append(current_node)
        return rte


def q_learning_rte(order, start, episodes=500):
    agent = QLearningAgent(order, start)
    for _ in range(episodes):
        agent.learn_episode()
    remaining_items = order[:]
    current_node = start
    rte = [current_node]
    while remaining_items:
        state = agent.get_state_key(current_node, remaining_items)
        if state in agent.Q:
            action = max(agent.Q[state], key=agent.Q[state].get)
            if action not in remaining_items:
                action = random.choice(remaining_items)
        else:
            action = random.choice(remaining_items)
        remaining_items.remove(action)
        rte.append(action)
        current_node = action
    return rte
