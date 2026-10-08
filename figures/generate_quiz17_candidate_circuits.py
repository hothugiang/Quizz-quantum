import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch


WIRE = "#668493"
EDGE = "#26333b"
BLUE = "#dceafb"
GREEN = "#ddf2e4"
PEACH = "#f7e1cf"
TEXT = "#111111"
YS = [3.25, 2.25, 0.95, -0.05]
QUBITS = [0, 1, 6, 7]


def setup():
    fig, ax = plt.subplots(figsize=(12, 4.05), dpi=180)
    ax.set_xlim(0, 12)
    ax.set_ylim(-0.55, 3.8)
    ax.axis("off")
    for qubit, y in zip(QUBITS, YS):
        ax.plot([1.65, 11.65], [y, y], color=WIRE, linewidth=1.8, zorder=1)
        ax.text(0.34, y, rf"$q_{qubit}$", ha="center", va="center", fontsize=19, color=TEXT)
        ax.text(1.05, y, r"$|0\rangle$", ha="center", va="center", fontsize=19, color=TEXT)
    ax.text(0.34, 1.6, r"$\vdots$", ha="center", va="center", fontsize=24, color=TEXT)
    ax.text(1.05, 1.6, r"$\vdots$", ha="center", va="center", fontsize=24, color=TEXT)
    return fig, ax


def gate(ax, x, y, label, face, width=2.2):
    height = 0.68
    patch = FancyBboxPatch(
        (x - width / 2, y - height / 2),
        width,
        height,
        boxstyle="round,pad=0.04,rounding_size=0.09",
        linewidth=1.6,
        edgecolor=EDGE,
        facecolor=face,
        zorder=3,
    )
    ax.add_patch(patch)
    ax.text(x, y, label, ha="center", va="center", fontsize=17, color=TEXT, zorder=4)


def rotation_layer(ax, names):
    xs = {1: [3.4], 2: [3.0, 5.35], 3: [2.7, 4.75, 6.8]}[len(names)]
    colors = [BLUE, GREEN, PEACH]
    for row, (qubit, y) in enumerate(zip(QUBITS, YS)):
        index = f"8b+{qubit}" if qubit else "8b"
        for x, name, color in zip(xs, names, colors):
            gate(ax, x, y, rf"${name}(\theta_{{{index}}})$", color, width=1.78 if len(names) == 3 else 2.15)
    ax.text(xs[-1] + 0.95, 1.6, r"$\vdots$", ha="center", va="center", fontsize=24, color=TEXT)


def dzz_pair(ax, x, y_top, y_bottom):
    ax.plot([x, x], [y_bottom, y_top], color=EDGE, linewidth=1.8, zorder=4)
    for y in (y_top, y_bottom):
        ax.add_patch(Circle((x, y), 0.075, facecolor=EDGE, edgecolor=EDGE, zorder=5))
    ax.text(x + 0.18, (y_top + y_bottom) / 2, r"$DZZ$", ha="left", va="center", fontsize=14, color=TEXT)


def dzz_layer(ax, x):
    dzz_pair(ax, x, YS[0], YS[1])
    dzz_pair(ax, x, YS[2], YS[3])
    ax.text(x, 1.6, r"$\vdots$", ha="center", va="center", fontsize=24, color=TEXT)


def cnot_pair(ax, x, control_y, target_y):
    ax.plot([x, x], [target_y, control_y], color=EDGE, linewidth=1.8, zorder=4)
    ax.add_patch(Circle((x, control_y), 0.075, facecolor=EDGE, edgecolor=EDGE, zorder=5))
    ax.add_patch(Circle((x, target_y), 0.15, facecolor="white", edgecolor=EDGE, linewidth=1.6, zorder=5))
    ax.plot([x - 0.105, x + 0.105], [target_y, target_y], color=EDGE, linewidth=1.5, zorder=6)
    ax.plot([x, x], [target_y - 0.105, target_y + 0.105], color=EDGE, linewidth=1.5, zorder=6)


def cnot_layer(ax, x):
    cnot_pair(ax, x, YS[0], YS[1])
    cnot_pair(ax, x, YS[2], YS[3])
    ax.text(x, 1.6, r"$\vdots$", ha="center", va="center", fontsize=24, color=TEXT)


def save(filename, rotations, interaction):
    fig, ax = setup()
    rotation_layer(ax, rotations)
    if interaction == "dzz":
        dzz_layer(ax, 9.35)
    elif interaction == "cnot":
        cnot_layer(ax, 9.35)
    fig.tight_layout(pad=0.15)
    fig.savefig(f"figures/{filename}.png", bbox_inches="tight", facecolor="white")
    fig.savefig(f"figures/{filename}.pdf", bbox_inches="tight", facecolor="white")
    plt.close(fig)


save("quiz17_ry_dzz_ansatz", ["RY"], "dzz")
save("quiz17_rxryrz_cnot_ansatz", ["RX", "RY", "RZ"], "cnot")
save("quiz17_ryrz_dzz_ansatz", ["RY", "RZ"], "dzz")
