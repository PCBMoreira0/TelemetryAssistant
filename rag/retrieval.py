from chromadb.types import Collection
from torch import Tensor


def search_vector_database(collection : Collection, query_embedding : Tensor, top_k: int = 3):

    results = collection.query(
        query_embeddings=[query_embedding.tolist()], n_results=top_k
    )

    return results
