from rag.loader import load_documents
from rag.splitter import split_documents
from rag.vector_db import generate_vector_db

documents = load_documents()
chunks = split_documents(loaded_documents=documents)
generate_vector_db(chunks=chunks)