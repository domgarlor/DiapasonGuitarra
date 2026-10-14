import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

names = ["C","C#/Db","D","D#/Eb","E","F","F#/Gb","G","G#/Ab","A","A#/Bb","B"]
strings = [("E",64),("B",59),("G",55),("D",50),("A",45),("E",40)]
PAGE, BOARD = "#444444", "#0b0b0b"
col = {"C":"#d00000","D":"#0030e0","E":"#000000","F":"#007a00","G":"#8000c0","A":"#7a4a1a","B":"#e0007a"}
bg = {2:"#ff9a66", 3:"#fff27a", 4:"#c8f0a8", 5:"#a8e0ff", 6:"#e0c0ff"}

fig, ax = plt.subplots(figsize=(26, 5.6), facecolor=PAGE)
ax.set_facecolor(PAGE)
ax.set_xlim(-1.6, 25.1); ax.set_ylim(-2.6, 7.4); ax.axis("off"); ax.set_aspect("equal")

ax.add_patch(Rectangle((0.5, 0), 24, 6, fc=BOARD, ec="none", zorder=0))
for i in range(6):                      # cuerdas
    ax.plot([0.5, 24.5], [5.5-i, 5.5-i], color="#6a6a6a", lw=0.9, zorder=1)
for f in range(1, 25):                  # trastes
    ax.plot([f+0.5]*2, [0, 6], color="#d8d8d8", lw=1.4, zorder=1)
ax.plot([0.5, 0.5], [0, 6], color="white", lw=5, zorder=2)   # cejuela

for r,(sname,base) in enumerate(strings):
    y = 5.5 - r
    ax.add_patch(Circle((-0.5, y), 0.4, fc=bg[base//12-1], ec="white", lw=2.2, zorder=3))
    ax.text(-0.5, y, sname, ha="center", va="center", fontsize=20, fontweight="bold", color=col[sname], zorder=4)
    for f in range(1, 25):
        m = base+f; n = names[m % 12]; o = m//12-1
        ax.add_patch(Circle((f, y), 0.4, fc=bg[o], ec="white", lw=2.2, zorder=3))
        if "/" not in n:
            ax.text(f, y, n, ha="center", va="center", fontsize=20, fontweight="bold", color=col[n], zorder=4)
        else:
            ax.text(f, y, n, ha="center", va="center", fontsize=7, fontweight="bold", color="#666666", zorder=4)

for f in (3,5,7,9,12,15,17,19,21,24):
    ax.text(f, 6.55, str(f), ha="center", va="center", fontsize=20, fontweight="bold", color="white")

for i,o in enumerate(sorted(bg)):
    x = 4.55 + i*3.4
    ax.add_patch(Circle((x, -1.1), 0.35, fc=bg[o], ec="white", lw=2))
    ax.text(x+0.6, -1.1, f"Octava {o}", ha="left", va="center", fontsize=14, color="white")
for i,n in enumerate("CDEFGAB"):
    x = 7.7 + i*1.6
    ax.add_patch(Circle((x, -2.1), 0.35, fc="#e8e8e8", ec="white", lw=2))
    ax.text(x, -2.1, n, ha="center", va="center", fontsize=16, fontweight="bold", color=col[n])
plt.savefig("diapason_guitarra_24_trastes_v2.png", dpi=110, bbox_inches="tight", facecolor=PAGE)
plt.savefig("diapason_guitarra_24_trastes_v2.pdf", bbox_inches="tight", facecolor=PAGE)
