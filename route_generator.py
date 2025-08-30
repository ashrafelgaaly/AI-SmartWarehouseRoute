
from warehouse import WarehouseGrid
from policies import naive_rte, greedy_rte, tsp_heur_rte, q_learning_rte


def generate_rte(order, policy="naive", start=(0, 0), episodes=500, speed=1):
    current_node = start
    rte = [start]

    if policy == "naive":
        visit_order = naive_rte(order, start)
    elif policy == "greedy":
        visit_order = greedy_rte(order, start)
    elif policy == "tsp":
        visit_order = tsp_heur_rte(order, start)
    elif policy == "q-learning":
        visit_order = q_learning_rte(order, start, episodes)
    else:
        raise ValueError("Unknown policy")

    total_distance = 0
    for node in visit_order:
        total_distance += WarehouseGrid.dist_calc(current_node, node)
        rte.append(node)
        current_node = node

    total_time = total_distance/speed

    return total_time, total_distance, rte
