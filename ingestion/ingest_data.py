# This file is to convert our documents into chunks and convert into vectors and store in the vectordb
from embeddings.embeddings import get_embedding_function
from retriever.retriever import retriever
from vectordb.chromadb import add_document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE,CHUNK_OVERLAP,DATA_DIR
from utils.document_loader import load_document

def ingest_data():
    # load the document
    raw_docs=load_document(DATA_DIR)
    if not raw_docs:
        return 0
    # split the document into chunks
    splitter=RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE,chunk_overlap=CHUNK_OVERLAP)
    splits=splitter.split_documents(raw_docs)
    
    # Differentiate the text and metadata
    texts=[d.page_content for d in splits]
    metadatas=[d.metadata for d in splits]
    
    # get the embedding function
    embedding_function=get_embedding_function()
    
    # add the document to the vectorstore
    add_document(texts,metadatas,embedding_function)    
    # return the number of chunks created just to do logging
    return len(splits)