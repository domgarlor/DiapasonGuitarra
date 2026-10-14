import colorsys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch

names = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
strings = [("E",64),("B",59),("G",55),("D",50),("A",45),("E",40)]
# fondo: un color pastel por octava
bg = {2:"#ffd0a8", 3:"#fff0a0", 4:"#c8f0a8", 5:"#a8e0ff", 6:"#e0c0ff"}
# letra: un color oscuro por nota (tonos separados por quintas para que semitonos vecinos contrasten)
fg = {}
for i,n in enumerate(names):
    fg[n] = colorsys.hls_to_rgb(((i*5)%12)/12, 0.26, 1.0)

fg = {"C":"#d00000","D":"#0030e0","E":"#000000","F":"#007a00","G":"#8000c0","A":"#7a4a1a","B":"#e0007a"}
W, H = 25, 6
fig, ax = plt.subplots(figsize=(26, 8.6))
ax.set_xlim(-1.0, W); ax.set_ylim(-3.6, H+2.0); ax.axis("off"); ax.set_aspect(0.7)

for r,(sname,base) in enumerate(strings):
    y = H-1-r
    for f in range(1,25):
        m = base+f; n = names[m%12]; o = m//12-1
        ax.add_patch(Rectangle((f-0.5, y), 1, 1, fc=bg[o], ec="#333", lw=1))
        if "#" not in n:
            ax.text(f, y+0.5, n, ha="center", va="center", fontsize=17, fontweight="bold", color=fg[n])
    ax.text(-0.1, y+0.5, sname, ha="center", va="center", fontsize=17, fontweight="bold", color=fg[sname])

marks = (3,5,7,9,12,15,17,19,21,24)
for f in range(1,25):
    ax.text(f, H+0.25, str(f), ha="center", va="center", fontsize=12, fontweight="bold" if f in marks else "normal")
for f in marks:
    ax.plot(f, -0.35, "o", color="#555", ms=10 if f in (12,24) else 8)
ax.text(12.5, H+1.5, "Guitarra eléctrica de 24 trastes – afinación estándar (E A D G B E)", ha="center", fontsize=18, fontweight="bold")
ax.text(-0.1, H+0.25, "Traste", ha="center", va="center", fontsize=10)

h1 = [Patch(fc=bg[o], ec="#333", label=f"Octava {o}") for o in sorted(bg)]
l1 = ax.legend(handles=h1, title="Color de fondo = octava", loc="lower center", ncol=5,
               bbox_to_anchor=(0.5,0.08), frameon=False, fontsize=12, title_fontsize=13)
ax.add_artist(l1)
nat = [n for n in names if "#" not in n]
h2 = [Patch(fc="white", ec="white", label=n) for n in nat]
l2 = ax.legend(handles=h2, title="Color de letra = nota", loc="lower center", ncol=7,
               bbox_to_anchor=(0.5,-0.06), frameon=False, fontsize=14, title_fontsize=13, handlelength=0.5)
for t,n in zip(l2.get_texts(), nat):
    t.set_color(fg[n]); t.set_fontweight("bold")
for ext in ("png", "pdf"):
    plt.savefig(f"diapason_guitarra_24_trastes.{ext}", dpi=130, bbox_inches="tight", facecolor="white")
