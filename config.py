from pathlib import Path

# Diretório base do projeto (onde está o config.py)
BASE_DIR = Path(__file__).resolve().parent

# Diretório base de dados (persistido via volume Docker)
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Documentos para indexação
DOCUMENTS_DIR = DATA_DIR / "documents"
DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)

# Persistência do ChromaDB
CHROMA_DIR = DATA_DIR / "chroma"
CHROMA_DIR.mkdir(parents=True, exist_ok=True)

# Modelos
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "llama3.2"

# Split de documentos
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
