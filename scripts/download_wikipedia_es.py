from pathlib import Path
from datasets import load_dataset

OUT = Path("data/raw/wikipedia_es.txt")
OUT.parent.mkdir(parents=True, exist_ok=True)

# Snapshot de Wikipedia en español, noviembre 2023
# Tarda unos minutos en arrancar la primera vez (baja metadata + índice)
print("Cargando dataset (puede tardar unos minutos)...")
ds = load_dataset(
    "wikimedia/wikipedia",
    "20231101.es",
    split="train",
    streaming=True,  # clave: NO baja todo, va leyendo
)

# Cuántos artículos procesar. Cada artículo ~10-30 KB.
# 5000 artículos ≈ 50-150 MB de texto
N_ARTICLES = 5000

print(f"Escribiendo {N_ARTICLES} artículos en {OUT}...")
with OUT.open("w", encoding="utf-8") as f:
    for i, art in enumerate(ds):
        if i >= N_ARTICLES:
            break
        f.write(art["text"].strip())
        f.write("\n\n")
        if (i + 1) % 500 == 0:
            print(f"  {i + 1}/{N_ARTICLES}...")

print(f"Listo. Tamaño: {OUT.stat().st_size / 1024 / 1024:.1f} MB")