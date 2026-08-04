from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.docstore.document import Document

from config import DOCS_DIR
import sys


def load_documents() -> list[Document]:
    pdf_files = list(DOCS_DIR.glob("*.pdf"))

    if not pdf_files:
        print(f"\n[AVISO] Nenhum arquivo PDF encontrado em: {DOCS_DIR}")
        print(
            "-> Por favor, adicione os manuais técnicos na pasta e tente novamente.\n"
        )
        sys.exit(1) 

    print(f"Carregando arquivos de: {DOCS_DIR}...")
    loader = PyPDFDirectoryLoader(str(DOCS_DIR))
    documents = loader.load()

    print(f"Total de páginas/documentos carregados: {len(documents)}")
    return documents
