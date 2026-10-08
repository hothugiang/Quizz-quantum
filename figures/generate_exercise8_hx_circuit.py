import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


fig, ax = plt.subplots(figsize=(10, 2.6), dpi=180)
ax.set_xlim(0, 10)
ax.set_ylim(-0.2, 2.2)
ax.axis("off")

wire_color = "#81919c"
label_color = "#17212b"
gate_edge = "#66849a"

ys = [1.55, 0.55]
for q, y in enumerate(ys):
    ax.plot([1.7, 9.25], [y, y], color=wire_color, linewidth=1.7, zorder=1)
    ax.text(0.55, y, rf"$q_{q}$", ha="center", va="center", fontsize=17, color=label_color)
    ax.text(1.28, y, r"$|0\rangle$", ha="center", va="center", fontsize=17, color=label_color)


def gate(x, y, text, face):
    width, height = 1.55, 0.60
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


gate(4.45, ys[0], r"$H$", "#dceafb")
gate(4.45, ys[1], r"$X$", "#ddf2e4")

fig.tight_layout(pad=0.2)
fig.savefig("figures/exercise8_hx_circuit.png", bbox_inches="tight", facecolor="white")
fig.savefig("figures/exercise8_hx_circuit.pdf", bbox_inches="tight", facecolor="white")
