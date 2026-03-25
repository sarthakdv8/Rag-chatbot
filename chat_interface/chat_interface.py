from rag_chain.ragchain import simple_rag_chain,get_load_document

# This function can be called at startup to display information about the RAG Chat Interface.
def startup_info():
    print("\n" + "=" * 55)
    print("RAG Chat Interface")
    print("=" * 55)
    
    docs=get_load_document()
    if docs:
        print(f"Loaded Documents ({len(docs)}):")
        for doc in docs:
            print(f" - {doc}")
    else:
        print("No documents found in the data directory.")  
    print("="*55 + "\n")
# This file provides a simple command-line interface to interact with the RAG chain.
def run_cli():
    # Initialize the RAG chain to a single variable
    chain=simple_rag_chain()
    print("Welcome to the RAG Chat Interface! Type 'exit' to quit.\n")
    startup_info()
    # Start a loop to continuously accept user input until they choose to exit
    while True:
        try:
            query=input("You:").strip()
        except(EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        if not query:
            continue
        if query.lower() in {"exit","quit"}:
            print("Goodbye!")
            break   
        result=chain.invoke({"input":query})
        answer=result.get("answer","")
        print(f"RAG Assistant:{answer}\n")