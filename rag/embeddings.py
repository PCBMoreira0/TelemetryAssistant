from sentence_transformers import SentenceTransformer

_model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    cache_folder="data/models"
)


def embed_documents(texts: list[str]):
    return _model.encode(texts)


def embed_query(query: str):
    query = query.lower().strip()
    return _model.encode(query)