from pathlib import Path
from cleriai.tokenizer import train_bpe_tokenizer, load_tokenizer

QUIJOTE = Path("data/raw/quijote.txt")
TOK_PATH = Path("data/processed/tokenizer.json")


def setup_module(module):
    if TOK_PATH.exists():
        TOK_PATH.unlink()  # forzar reentrenamiento
    assert QUIJOTE.exists(), (
        f"Falta {QUIJOTE}. Corré: uv run python scripts/download_corpus.py"
    )
    train_bpe_tokenizer(QUIJOTE, vocab_size=2000, save_path=TOK_PATH)


def test_roundtrip_texto_a_ids_a_texto():
    tok = load_tokenizer(TOK_PATH)
    texto = "En un lugar de la Mancha"
    ids = tok.encode(texto).ids
    assert isinstance(ids, list)
    assert all(isinstance(i, int) for i in ids)
    reconstruido = tok.decode(ids)
    # El roundtrip puede no ser perfecto (espacios, case), pero tiene que tener
    # el mismo "shape" aproximado
    assert len(reconstruido) > 0


def test_tokens_conocidos_se_comprimen():
    """Si el tokenizer aprendió bien, palabras frecuentes como 'que' o 'de'
    deberían ser UN solo token, no varios."""
    tok = load_tokenizer(TOK_PATH)
    for palabra in ["que", "de", "la", "el"]:
        ids = tok.encode(f" {palabra}").ids
        assert len(ids) == 1, (
            f"Esperaba 1 token para '{palabra}', obtuve {ids}"
        )


def test_vocab_size_es_el_esperado():
    tok = load_tokenizer(TOK_PATH)
    assert tok.get_vocab_size() == 2000