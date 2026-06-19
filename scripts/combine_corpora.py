from pathlib import Path

OUT = Path("data/raw/corpus_combined.txt")
parts = [
    Path("data/raw/quijote.txt"),
    Path("data/raw/wikipedia_es.txt"),
]

with OUT.open("w", encoding="utf-8") as out:
    for p in parts:
        if not p.exists():
            print(f"⚠️  Falta {p}, saltando")
            continue
        text = p.read_text(encoding="utf-8")
        out.write(text)
        out.write("\n\n")
        print(f"  + {p.name}: {len(text):,} chars")

print(f"\nTotal: {OUT.stat().st_size / 1024 / 1024:.1f} MB en {OUT}")