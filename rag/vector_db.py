from chromadb import Collection, PersistentClient
from langchain_community.docstore.document import Document
from rag.embeddings import embed_documents

client = PersistentClient(path="data/chroma")

def get_collection() -> Collection:
    client = PersistentClient(path="data/chroma")

    collection = client.get_collection("boat_docs")

    return collection


def generate_vector_db(chunks: list[Document]):

    collection = client.get_or_create_collection("boat_docs")

    ids = [chunk.id for chunk in chunks]
    documents = [chunk.page_content for chunk in chunks]
    metadatas = [chunk.metadata for chunk in chunks]
    embeddings = embed_documents(documents)

    collection.upsert(
        ids=ids,
        embeddings= embeddings.tolist(),
        documents=documents,
        metadatas=metadatas,
    )
