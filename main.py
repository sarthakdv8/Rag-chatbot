import argparse
from chat_interface.chat_interface import run_cli,startup_info
from ingestion.ingest_data import ingest_data


def main():
    print("main.py is running")
    parser=argparse.ArgumentParser()
    parser.add_argument("--ingest",action="store_true",help="Ingest document before starting the chat interface")
    args=parser.parse_args()
    print("main.py is running before if clause")
    
    if args.ingest:
        print("main.py is running")
        n=ingest_data()
        print("main.py is running")
        print(f"Ingested {n} chunks ")

    run_cli()
    
    
if __name__=="__main__":    
    main()
        
        
