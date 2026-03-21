from langchain_community.embeddings import SentenceTransformerEmbeddings

from config import EMBEDDING_MODEL_NAME

# Make the function for embedding funcion that i can use in other folders
def get_embedding_function():
    return SentenceTransformerEmbeddings(model_name=EMBEDDING_MODEL_NAME)