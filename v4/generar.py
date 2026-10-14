import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import Circle, Rectangle

names = ["C","C#/Db","D","D#/Eb","E","F","F#/Gb","G","G#/Ab","A","A#/Bb","B"]
strings = [("E",64),("B",59),("G",55),("D",50),("A",45),("E",40)]
PAGE, BOARD = "#444444", "#0b0b0b"
col = {"C":"#d00000","D":"#0030e0","E":"#000000","F":"#007a00","G":"#00757a","A":"#ffffff","B":"#4b0a8c"}
# fondo = distancia tonal respecto a A (I = A, III mayor = C#, V = E, VII = G; resto neutro; otros sostenidos oscuros)
deg = {"A":"#2a6fd6", "C":"#cfcfcf", "E":"#8fe3a0", "G":"#ff9ec4", "B":"#cfcfcf", "D":"#cfcfcf", "F":"#cfcfcf"}
SHARP, TERCERA = "#1c1c1c", "#ffa94d"
def fondo(n):
    if n == "C#/Db":
        return TERCERA
    return SHARP if "/" in n else deg[n]

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
    ax.add_patch(Circle((-0.5, y), 0.4, fc=deg[sname], ec="white", lw=2.2, zorder=3))
    ax.text(-0.5, y, sname, ha="center", va="center", fontsize=20, fontweight="bold", color=col[sname], zorder=4)
    for f in range(1, 25):
        m = base+f; n = names[m % 12]; o = m//12-1
        ax.add_patch(Circle((f, y), 0.4, fc=fondo(n), ec="white", lw=2.2, zorder=3))
        if "/" not in n:
            ax.text(f, y, n, ha="center", va="center", fontsize=20, fontweight="bold", color=col[n], zorder=4)
        else:
            ax.text(f, y, n, ha="center", va="center", fontsize=7, fontweight="bold", color=("#222222" if n == "C#/Db" else "#9a9a9a"), zorder=4)

# líneas que separan las octavas (bordes entre casillas de distinta octava)
def octv(r, f):
    return (strings[r][1] + f) // 12 - 1
for r in range(6):
    y = 5.5 - r
    for f in range(1, 25):
        if f < 24 and octv(r, f) != octv(r, f+1):
            ax.plot([f+0.5]*2, [y-0.5, y+0.5], color="#ffd54a", lw=4, solid_capstyle="round", zorder=2.5)
        if r < 5 and octv(r, f) != octv(r+1, f):
            ax.plot([f-0.5, f+0.5], [y-0.5]*2, color="#ffd54a", lw=4, solid_capstyle="round", zorder=2.5)

for f in (3,5,7,9,12,15,17,19,21,24):
    ax.text(f, 6.55, str(f), ha="center", va="center", fontsize=15, fontweight="bold", color="white")

items = [("I (A)", deg["A"]), ("III (C#)", TERCERA), ("V (E)", deg["E"]), ("VII (G)", deg["G"]), ("Otras notas", "#cfcfcf")]
for i,(txt,c) in enumerate(items):
    x = 4.55 + i*3.4
    ax.add_patch(Circle((x, -1.1), 0.35, fc=c, ec="white", lw=2))
    ax.text(x+0.6, -1.1, txt, ha="left", va="center", fontsize=14, color="white")
for i,n in enumerate("CDEFGAB"):
    x = 7.7 + i*1.6
    ax.add_patch(Circle((x, -2.1), 0.35, fc="#e8e8e8", ec="white", lw=2))
    t = ax.text(x, -2.1, n, ha="center", va="center", fontsize=16, fontweight="bold", color=col[n])
    if n == "A":
        t.set_path_effects([pe.withStroke(linewidth=3, foreground="#333333")])
plt.savefig("diapason_guitarra_24_trastes_v4.png", dpi=110, bbox_inches="tight", facecolor=PAGE)
plt.savefig("diapason_guitarra_24_trastes_v4.pdf", bbox_inches="tight", facecolor=PAGE)
