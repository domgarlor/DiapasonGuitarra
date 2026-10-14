# Diapasón de guitarra eléctrica de 24 trastes

Imágenes (PNG y PDF) con todas las notas de una guitarra eléctrica de 24 trastes en afinación estándar (E A D G B E), generadas con Python y matplotlib.

- `v1/`: tabla rectangular. Fondo de casilla = octava, color de letra = nota, sostenidos sin texto.
- `v2/`: estilo de mástil oscuro con círculos. Misma lógica de colores, con los sostenidos en gris pequeño (C#/Db…).
- `v3/`: como la V2, con fondos de octava verde/lila/naranja/lima/azul, líneas amarillas que separan las octavas y colores de nota ajustados para que se lean (A en blanco, B morado).
- `v4/`: como la V3, pero el fondo indica la distancia tonal respecto a A: I (A), III mayor (C#), V (E) y VII (G), es decir, el acorde A7.

## Regenerar

```bash
cd v1 && python3 generar.py
cd ../v2 && python3 generar.py
cd ../v3 && python3 generar.py
cd ../v4 && python3 generar.py
```

Requiere `matplotlib`.
