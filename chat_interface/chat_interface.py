from rag_chain.ragchain import simple_rag_chain

# This file provides a simple command-line interface to interact with the RAG chain.
def run_cli():
    # Initialize the RAG chain to a single variable
    chain=simple_rag_chain()
    print("Welcome to the RAG Chat Interface! Type 'exit' to quit.\n")
    # Start a loop to continuously accept user input until they choose to exit
    while True:
        try:
            query=input("You:").strip()
        except:
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