# Diapasón de guitarra eléctrica de 24 trastes

Imágenes (PNG y PDF) con todas las notas de una guitarra eléctrica de 24 trastes en afinación estándar (E A D G B E), generadas con Python y matplotlib.

- `v1/`: tabla rectangular. Fondo de casilla = octava, color de letra = nota, sostenidos sin texto.
- `v2/`: estilo de mástil oscuro con círculos. Misma lógica de colores, con los sostenidos en gris pequeño (C#/Db…).

## Regenerar

```bash
cd v1 && python3 generar.py
cd ../v2 && python3 generar.py
```

Requiere `matplotlib`.
