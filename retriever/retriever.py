#  This file is used to get the data from the vector based on our query.



from embeddings.embeddings import get_embedding_function
from vectordb.chromadb import get_vectorstore
from config import TOP_K

def retriever():
    embeddings=get_embedding_function()
    vs=get_vectorstore(embeddings)
    # a method in langchain to get the similiarity based retriever
    vs.as_retriever(search_type="similarity",search_kwargs={"k":TOP_K})