"""
UCB (Upper Confidence Bound) visualization for Chapter 10.
Generates: docs/public/figures/ch10_fig2_ucb_tradeoff.png
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

sns.set_theme(style="whitegrid", font_scale=1.15)
plt.rcParams.update({
    "figure.dpi": 150,
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
})

# ── colour palette ──────────────────────────────────────────────────────────
C_EXPLOIT = "#4C8CBF"   # blue  – exploitation term
C_EXPLORE = "#E07B54"   # orange – exploration term
C_UCB     = "#2CA02C"   # green  – total UCB
C_OPT     = "#9467BD"   # purple – optimal c line

# ── figure layout: 1 row × 3 cols ───────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(16, 5.2),
                          gridspec_kw={"width_ratios": [1.6, 1.6, 1]})
fig.suptitle("UCB: The Mathematics of Exploration vs. Exploitation",
             fontsize=15, fontweight="bold", y=1.02)

# ════════════════════════════════════════════════════════════════════════════
# Panel A: UCB components vs visit count
# ════════════════════════════════════════════════════════════════════════════
ax = axes[0]
N_parent = 1000          # total simulations so far
n_visits  = np.linspace(1, N_parent, 400)
c = np.sqrt(2)

win_rate  = 0.55         # fixed exploitation value for illustration
exploit   = np.full_like(n_visits, win_rate)
explore   = c * np.sqrt(np.log(N_parent) / n_visits)
ucb_total = exploit + explore

ax.plot(n_visits, exploit,   color=C_EXPLOIT, lw=2.2, label="Exploitation  $w/n$")
ax.plot(n_visits, explore,   color=C_EXPLORE, lw=2.2, linestyle="--",
        label=r"Exploration  $c\,\sqrt{\ln N / n}$")
ax.plot(n_visits, ucb_total, color=C_UCB,     lw=2.5, linestyle="-.",
        label="Total UCB")

ax.axvline(x=80, color="grey", lw=1.2, linestyle=":")
ax.text(85, 2.3, "Transition\npoint", color="grey", fontsize=9.5, va="top")

ax.fill_between(n_visits, exploit, ucb_total,
                alpha=0.10, color=C_EXPLORE, label="_nolegend_")

ax.set_xlabel("Node visit count  $n$", fontsize=11)
ax.set_ylabel("Score", fontsize=11)
ax.set_title("Panel A  –  UCB Decomposition\n($N=1000$, $c=\\sqrt{2}$)", fontsize=11)
ax.legend(fontsize=9.5, loc="upper right")
ax.set_xlim(1, N_parent)
ax.set_ylim(0, 2.8)

# ════════════════════════════════════════════════════════════════════════════
# Panel B: Effect of c on exploration–exploitation balance
# ════════════════════════════════════════════════════════════════════════════
ax = axes[1]
n = np.linspace(1, 500, 400)
N = 500
win = 0.55

palette = sns.color_palette("viridis", 5)
c_vals  = [0.2, 0.7, np.sqrt(2), 2.5, 4.0]
labels  = ["$c=0.2$  (greedy)", "$c=0.7$", r"$c=\sqrt{2}$  (standard)",
           "$c=2.5$", "$c=4.0$  (exploratory)"]

for ci, label, col in zip(c_vals, labels, palette):
    ucb = win + ci * np.sqrt(np.log(N) / n)
    lw  = 2.8 if abs(ci - np.sqrt(2)) < 0.01 else 1.8
    ls  = "-" if abs(ci - np.sqrt(2)) < 0.01 else "--"
    ax.plot(n, ucb, color=col, lw=lw, linestyle=ls, label=label)

ax.set_xlabel("Node visit count  $n$", fontsize=11)
ax.set_ylabel("UCB score", fontsize=11)
ax.set_title("Panel B  –  Effect of Exploration Constant $c$\n($N=500$, $w/n=0.55$)", fontsize=11)
ax.legend(fontsize=9, loc="upper right")
ax.set_xlim(1, 500)

# ════════════════════════════════════════════════════════════════════════════
# Panel C: Conceptual bar chart – visit distribution under UCB
# ════════════════════════════════════════════════════════════════════════════
ax = axes[2]

nodes      = ["A\n(win=0.8)", "B\n(win=0.6)", "C\n(win=0.4)", "D\n(win=0.2)"]
visits     = [410, 220, 80, 40]        # approximate UCB-guided distribution
win_rates  = [0.8, 0.6, 0.4, 0.2]

bar_colors = [sns.color_palette("RdYlGn", 10)[int(w * 9)] for w in win_rates]

bars = ax.barh(nodes[::-1], visits[::-1], color=bar_colors[::-1],
               edgecolor="white", linewidth=0.8, height=0.55)

for bar, v, w in zip(bars, visits[::-1], win_rates[::-1]):
    ax.text(bar.get_width() + 8, bar.get_y() + bar.get_height() / 2,
            f"{v} visits\n(w={w:.1f})", va="center", fontsize=9, color="#333333")

ax.set_xlabel("Simulation count", fontsize=11)
ax.set_title("Panel C  –  Visit Distribution\n(UCB budget = 750)", fontsize=11)
ax.set_xlim(0, 530)
ax.tick_params(axis="y", labelsize=10)

# colour bar as legend
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.cm as cm_lib
cmap = LinearSegmentedColormap.from_list("rg", ["#d73027", "#ffffbf", "#1a9850"])
sm   = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(0, 1))
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, orientation="vertical", fraction=0.05, pad=0.02)
cbar.set_label("Win rate", fontsize=9)
cbar.set_ticks([0, 0.5, 1])
cbar.set_ticklabels(["0.0", "0.5", "1.0"])

# ── shared footnote ──────────────────────────────────────────────────────────
fig.text(0.5, -0.03,
         r"UCB formula:  $\mathrm{UCB}(n)=\dfrac{w_n}{n}+c\,\sqrt{\dfrac{\ln N}{n}}$"
         "    |    Proven to converge to optimal policy at O(log N) regret  "
         "[Kocsis & Szepesvári, 2006]",
         ha="center", fontsize=9.5, color="#555555")

plt.tight_layout(rect=[0, 0.02, 1, 1])

out = "/Users/lizixi/Desktop/ReasoningKingdom/Reasoning-Kingdom/docs/public/figures/ch10_fig2_ucb_tradeoff.png"
plt.savefig(out, dpi=150, bbox_inches="tight")
print(f"Saved → {out}")
