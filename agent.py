from rag.embeddings import embed_query
from rag.retrieval import search_vector_database
from rag.vector_db import get_collection

collection = get_collection()

query = embed_query("What the voltage that may explode the battery?")

results = search_vector_database(
    collection=collection,
    query_embedding=query,
)

context = "\n\n".join(results['documents'][0])
print(context)