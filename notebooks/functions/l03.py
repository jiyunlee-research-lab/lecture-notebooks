import numpy as np
import matplotlib.pyplot as plt

# Color definitions
BLUE = "#2a78d6"
RED = "#e34948"
INK = "#0b0b0b"
MUTED = "#52514e"

# Computes the utility of each point from its indifference probability P* and plots the utility function
def utility(best_outcome, worst_outcome, points, plot=True):
    x_best, u_best = best_outcome
    x_worst, u_worst = worst_outcome

    results = [(x, u_best * p + u_worst * (1 - p)) for x, p in points]
    results = sorted([worst_outcome, best_outcome] + results)

    if plot:
        x, u = zip(*results)

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot([x_worst, x_best], [u_worst, u_best], color=MUTED, linestyle="--", linewidth=1, label="Risk neutral")
        ax.plot(x, u, color=BLUE, linewidth=2, marker="o", markersize=7, label="Your utility function")

        ax.set_xlabel(r"Outcome $X$ (\$)", color=INK)
        ax.set_ylabel(r"Utility $u(X)$", color=INK)
        ax.set_title("Utility function", fontsize=13, color=INK, fontweight="bold")
        ax.legend()
        ax.grid(alpha=0.2)
        plt.show()

    return results