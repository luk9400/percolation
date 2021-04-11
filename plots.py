import matplotlib.pyplot as plt

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
plt.savefig("fig1")
