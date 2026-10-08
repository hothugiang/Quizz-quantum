import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle


fig, ax = plt.subplots(figsize=(11, 3.4), dpi=180)
ax.set_xlim(0, 11)
ax.set_ylim(-0.2, 3.2)
ax.axis("off")

wire_color = "#81919c"
label_color = "#17212b"
gate_edge = "#66849a"
ys = [2.45, 1.45, 0.45]

for q, y in enumerate(ys):
    ax.plot([1.75, 10.25], [y, y], color=wire_color, linewidth=1.7, zorder=1)
    ax.text(0.55, y, rf"$q_{q}$", ha="center", va="center", fontsize=17, color=label_color)
    ax.text(1.30, y, r"$|0\rangle$", ha="center", va="center", fontsize=17, color=label_color)


def box_gate(x, y, text, face):
    width, height = 1.25, 0.58
    patch = FancyBboxPatch(
        (x - width / 2, y - height / 2),
        width,
        height,
        boxstyle="round,pad=0.03,rounding_size=0.035",
        linewidth=1.5,
        edgecolor=gate_edge,
        facecolor=face,
        zorder=3,
    )
    ax.add_patch(patch)
    ax.text(x, y, text, ha="center", va="center", fontsize=17, color=label_color, zorder=4)


def cnot(x, control_y, target_y):
    ax.plot([x, x], [target_y, control_y], color=label_color, linewidth=1.7, zorder=2)
    ax.add_patch(Circle((x, control_y), 0.075, facecolor=label_color, edgecolor=label_color, zorder=4))
    ax.add_patch(Circle((x, target_y), 0.19, facecolor="white", edgecolor=label_color, linewidth=1.6, zorder=4))
    ax.plot([x - 0.14, x + 0.14], [target_y, target_y], color=label_color, linewidth=1.5, zorder=5)
    ax.plot([x, x], [target_y - 0.14, target_y + 0.14], color=label_color, linewidth=1.5, zorder=5)


box_gate(3.25, ys[0], r"$H$", "#dceafb")
cnot(5.65, ys[0], ys[1])
cnot(8.05, ys[1], ys[2])

fig.tight_layout(pad=0.2)
fig.savefig("figures/exercise10_ghz_circuit.png", bbox_inches="tight", facecolor="white")
fig.savefig("figures/exercise10_ghz_circuit.pdf", bbox_inches="tight", facecolor="white")
