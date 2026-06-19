# cleri-ai

Mini-LLM en español con tool-use (function calling).

## Setup
- Instalar `uv`
- `uv sync`
- `uv run pytest`

## Estructura
- `src/cleriai/` — código del modelo y del runtime
- `data/raw/` — corpus original
- `data/processed/` — datos tokenizados
- `checkpoints/` — modelos entrenados
- `tests/` — tests automatizados