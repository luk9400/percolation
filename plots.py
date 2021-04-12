import matplotlib.pyplot as plt


def fig_b():
    markers = {"10": "o", "50": "s", "100": "^"}

    for i in [10, 50, 100]:
        with open(f"./tests/Ave_L{i}T10000.txt", "r") as f:
            lines = f.readlines()
            xs = []
            ys = []
            for line in lines:
                values = line.split("  ")

                xs.append(float(values[0]))
                ys.append(float(values[1]))
            plt.scatter(xs, ys, label=f"L = {i}", marker=markers[str(i)])

    plt.xlabel("p")
    plt.ylabel("$p_{flow}$")
    plt.legend()
    plt.grid()
    plt.savefig("fig_b")


def fig_c():
    markers = {"10": "o", "50": "s", "100": "^"}

    for i in [10, 50, 100]:
        with open(f"./tests/Ave_L{i}T10000.txt", "r") as f:
            lines = f.readlines()
            xs = []
            ys = []
            for line in lines:
                values = line.split("  ")

                xs.append(float(values[0]))
                ys.append(float(values[2]))
            plt.scatter(xs, ys, label=f"L = {i}", marker=markers[str(i)])

    plt.xlabel("p")
    plt.ylabel("$p_{flow}$")
    plt.legend()
    plt.grid()
    plt.savefig("fig_c")


def fig_d():
    markers = ["1", "2", "3", "4", "o", "s", "^", "+"]

    for idx, i in enumerate([0.2, 0.3, 0.4, 0.5, 0.592746, 0.6, 0.7, 0.8]):
        with open(f"./tests/Dist_p{i}L100T10000.txt", "r") as f:
            lines = f.readlines()
            xs = []
            ys = []
            for line in lines:
                values = line.split("  ")

                xs.append(float(values[0]))
                ys.append(float(values[1]))
            plt.scatter(xs, ys, label=f"p = {i}", marker=markers[idx])

    plt.xlabel("s")
    plt.ylabel("n(s, p, 100)")
    plt.grid()
    plt.legend()
    plt.yscale("log")
    plt.savefig("fig_dL100")


# fig_b()
# fig_c()
fig_d()
