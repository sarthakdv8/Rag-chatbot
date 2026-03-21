from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env file

load_dotenv()

# base directory of the project
BASE_DIR=Path(__file__).parent
DATA_DIR=BASE_DIR/"data"
CHROMA_DIR=DATA_DIR/".chromadb"

# Models
EMBEDDING_MODEL_NAME="sentence-transformers/all-MiniLM-L6-v2"

# GROQ
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
GROQ_MODEL_NAME = os.getenv("GROQ_MODEL_NAME")

# CHUNKING
CHUNK_SIZE=500
CHUNK_OVERLAP=50

# retrival top k documents
TOP_K=4


# Ensure the data directory exists
DATA_DIR.mkdir(parents=True, exist_ok=True)
CHROMA_DIR.mkdir(parents=True, exist_ok=True) 