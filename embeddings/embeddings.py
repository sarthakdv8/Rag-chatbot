from langchain_community.embeddings import SentenceTransformerEmbedding

from config import EMBEDDING_MODEL_NAME

def get_embedding_function():
    return SentenceTransformerEmbedding(model_name=EMBEDDING_MODEL_NAME)