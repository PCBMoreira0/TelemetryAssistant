from chromadb import Collection, PersistentClient
from langchain_community.docstore.document import Document
from rag.embeddings import embed_documents

import config 

_client = PersistentClient(path=config.CHROMA_DIR)

def get_collection(name: str = "boat_docs") -> Collection:
    return _client.get_or_create_collection(name)

def generate_vector_db(chunks: list[Document]):

    collection = _client.get_or_create_collection("boat_docs")

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
