from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.docstore.document import Document


def load_documents() -> list[Document]:
    loader = PyPDFDirectoryLoader("data/docs/")
    documents = loader.load()

    print(f"Total de páginas/documentos carregados: {len    (documents)}")

    return documents
