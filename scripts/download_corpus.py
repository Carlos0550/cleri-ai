import urllib.request
from pathlib import Path

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

URL = "https://www.gutenberg.org/cache/epub/2000/pg2000.txt"
DEST = RAW_DIR / "quijote.txt"

if not DEST.exists():
    print(f"Bajando {URL}...")
    urllib.request.urlretrieve(URL, DEST)
    print(f"Guardado en {DEST}")
else:
    print(f"Ya existe {DEST}")
print(f"Tamaño: {DEST.stat().st_size / 1024:.1f} KB")