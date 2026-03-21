import argparse
from chat_interface.chat_interface import run_cli
from ingestion.ingest_data import ingest_data


def main():
    parser=argparse.Argumentparser()
    parser.add_argument("--ingest",action="store_true",help="Ingest document before starting the chat interface")
    args=parser.parse_args()
    
    if args.ingest_data:
        n=ingest_data()
        print(f"Ingested {n} chunks ")
        
    run_cli()
    
    if __name__=="__main__":
        main()
        