from langchain_community.vectorstores import Chroma

from config import CHROMA_DIR

# Directing Chroma to use the specified directory for storing its data

def get_vectorstore(embedding_function):
    return Chroma(embedding_function=embedding_function,persist_directory=str(CHROMA_DIR))

# Adding document to the vectorstore

def add_document(texts,metdatas,embedding_function):
    vs=Chroma.from_texts(
        texts=texts,
        metadatas=metdatas,
        embedding_function=embedding_function,
        persist_directory=str(CHROMA_DIR)
    )
    vs.persist()
    return vs