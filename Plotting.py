
import matplotlib.pyplot as plt


def plot_route(rte, order_points, warehouse_size=(10,10), policy=''):
    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_xlim(-1, warehouse_size[0])
    ax.set_ylim(-1, warehouse_size[1])
    ax.set_xticks(range(warehouse_size[0]+1))
    ax.set_yticks(range(warehouse_size[1]+1))
    ax.grid(True)

    xs, ys = zip(*rte)
    ax.plot(xs, ys, color="blue", linewidth=2, marker="o")

    for i, (x, y) in enumerate(rte):
        ax.text(x, y+0.2, str(i), color="red", fontsize=10, ha="center")

    ox, oy = zip(*order_points)
    ax.scatter(ox, oy, c="green", s=100, marker="s", label="Order Items")

    ax.scatter(rte[0][0], rte[0][1], c="orange", s=120, marker="*", label="Start")

    ax.legend()
    ax.set_title(policy)
    plt.show()
