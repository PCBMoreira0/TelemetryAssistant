from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.docstore.document import Document


def split_documents(
    loaded_documents: list[Document], chunk_size: int = 300, chunk_overlap: int = 60
) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""],
    )

    chunks = splitter.split_documents(loaded_documents)

    for i, chunk in enumerate(chunks):
        chunk.id = f"{chunk.metadata['source']}_chunk_{i}"

    print(f"Total de chunks gerados: {len(chunks)}")
    return chunks
