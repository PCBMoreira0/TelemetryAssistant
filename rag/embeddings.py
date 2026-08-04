from sentence_transformers import SentenceTransformer

import config

_model = SentenceTransformer(
    config.EMBEDDING_MODEL,
    cache_folder=config.MODELS_DIR
)


def embed_documents(texts: list[str]):
    return _model.encode(texts)


def embed_query(query: str):
    query = query.lower().strip()
    return _model.encode(query)