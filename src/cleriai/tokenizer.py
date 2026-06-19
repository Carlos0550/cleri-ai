from pathlib import Path
from tokenizers import Tokenizer, models, trainers, pre_tokenizers, decoders

def train_bpe_tokenizer(
    text_path: Path,
    vocab_size: int = 8000,
    save_path: Path = None,
) -> Tokenizer:
    tokenizer = Tokenizer(models.BPE(unk_token=None))

    tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()

    tokenizer.decoder = decoders.BPEDecoder()

    trainer = trainers.BpeTrainer(
        vocab_size=vocab_size,
        special_tokens=["<pad>", "<bos>", "<eos>", "<unk>"],
        show_progress=True,
    )

    tokenizer.train(files=[str(text_path)], trainer=trainer)


    if save_path is not None:
        save_path.parent.mkdir(parents=True, exist_ok=True)
        tokenizer.save(str(save_path))
        print(f"Tokenizer guardado en {save_path}")

    return tokenizer


def load_tokenizer(path: Path) -> Tokenizer:
    return Tokenizer.from_file(str(path))

if __name__ == "__main__":
    quijote = Path("data/raw/quijote.txt")
    out = Path("data/processed/tokenizer.json")
    tok = train_bpe_tokenizer(quijote, vocab_size=8000, save_path=out)
    print(f"Vocab size final: {tok.get_vocab_size()}")