
from route_generator import generate_rte
from Plotting import plot_route

if __name__ == "__main__":
    warehouse_size = (10, 10)
    start = (7, 7)
    order = [(2, 2), (4, 1), (1, 5), (6, 4), (9, 3)]

    for policy in ["naive", "greedy", "tsp", "q-learning"]:
        time, dist, route = generate_rte(order, policy=policy, start=start, episodes=500)
        print(f"\nPolicy: {policy}")
        print("Total Time:", time)
        print("Total Distance:", dist)
        print("Route:", route)

        plot_route(route, order_points=order, warehouse_size=warehouse_size, policy=policy)
