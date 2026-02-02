from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter


from config import CHROMA_DIR, CHUNK_SIZE, CHUNK_OVERLAP
from rag.embeddings import get_embeddings


def create_vectorstore(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    chunks = splitter.split_documents(documents)

    return Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory=str(CHROMA_DIR)
    )


def load_vectorstore():
    return Chroma(
        persist_directory=str(CHROMA_DIR),
        embedding_function=get_embeddings()
    )
