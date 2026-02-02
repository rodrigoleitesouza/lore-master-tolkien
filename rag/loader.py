from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredMarkdownLoader,
    Docx2txtLoader,
)

LOADERS = {
    ".pdf": PyPDFLoader,
    ".txt": TextLoader,
    ".md": UnstructuredMarkdownLoader,
    ".docx": Docx2txtLoader,
}

def load_documents(directory: Path):
    documents = []
    for file in directory.glob("**/*"):
        if file.suffix.lower() in LOADERS:
            loader = LOADERS[file.suffix.lower()](str(file))
            documents.extend(loader.load())
    return documents
