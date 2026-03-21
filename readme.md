









PROJECT STRUCTURE
Rag-Folder/
├── data/
│   └── documents/
├── embeddings/
│   └── embedding_model.py
├── vectordb/
│   └── chroma_store.py
├── ingestion/
│   └── ingest_data.py
├── retriever/
│   └── retriever.py
├── chains/
│   └── rag_chain.py
├── chatbot/
│   └── chat_interface.py
├── utils/
│   └── document_loader.py
├── config.py
├── requirements.txt
├── main.py
└── README.md
```

We use chroma as our vectorstore for storing our data

We use the all-MiniLM-L6-v2 sentence transformer model to create embeddings

We use RecursiveCharacterTextSplitter to split our documents into chunks

We use Groq model to generate responses

We use LangChain to create a chatbot

We have rag_chain.py to create a rag chain and give the instruction and better citation to the file so that the answers will not hallucinate and give user the better context and citation.

chat_interface.py to create a simple command-line interface to interact with the RAG chain