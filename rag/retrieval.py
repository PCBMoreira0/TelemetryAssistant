from chromadb.types import Collection
from torch import Tensor

from rag.vector_db import get_collection


def search_vector_database(query_embedding: Tensor, top_k: int = 5):
    collection = get_collection()
    results = collection.query(
        query_embeddings=[query_embedding.tolist()], n_results=top_k
    )

    search_results = []

    for doc_id, document, metadata in zip(
        results["ids"][0],
        results["documents"][0],
        results["metadatas"][0],
    ):
        search_results.append(
            {
                "id": doc_id,
                "content": document,
                "metadata": metadata,
            }
        )

    return search_results
