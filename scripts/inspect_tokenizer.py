from pathlib import Path
from cleriai.tokenizer import load_tokenizer

tok = load_tokenizer(Path("data/processed/tokenizer.json"))

# Probá codificar algunas frases
frases = [
    "Hola, ¿cómo estás?",
    "El Quijote es un libro famoso.",
    "La programación es divertida.",
    "ñandú, árbol, pájaro",
]

for frase in frases:
    encoded = tok.encode(frase)
    print(f"\nFrase: {frase!r}")
    print(f"  IDs: {encoded.ids}")
    print(f"  Tokens: {encoded.tokens}")
    print(f"  Cantidad: {len(encoded.ids)}")

# Probá decodificar
ids = [1, 50, 200, 500, 1000]
print(f"\nDecodificando {ids}: {tok.decode(ids)!r}")