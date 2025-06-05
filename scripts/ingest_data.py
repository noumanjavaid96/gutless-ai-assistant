# scripts/ingest_data.py
import argparse
import os
import sys

# Add src to Python path to allow importing modules from src
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(os.path.dirname(current_dir), 'src')
sys.path.append(src_path)

from content_ingestion.ingest import process_and_ingest_content # type: ignore
from pinecone_service import initialize_pinecone # type: ignore
from config.settings import PINECONE_INDEX_NAME, PINECONE_EMBEDDING_DIMENSION # type: ignore
import pinecone # type: ignore

def main():
    parser = argparse.ArgumentParser(description="Ingest content into Pinecone for Gutless AI Assistant.")
    parser.add_argument("file_path", type=str, help="Path to the content file (e.g., PDF, audio file path for transcription).")
    parser.add_argument("content_type", type=str, choices=["pdf", "audio", "text"], help="Type of the content.")
    # Add more arguments as needed, e.g., for metadata

    args = parser.parse_args()

    print("Initializing Pinecone connection...")
    try:
        initialize_pinecone()
        # Check if index exists, create if not (for script convenience, might differ from bot logic)
        if PINECONE_INDEX_NAME not in pinecone.list_indexes():
            print(f"Pinecone index '{PINECONE_INDEX_NAME}' not found. Creating it with dimension {PINECONE_EMBEDDING_DIMENSION}...")
            pinecone.create_index(PINECONE_INDEX_NAME, dimension=PINECONE_EMBEDDING_DIMENSION)
            print(f"Index '{PINECONE_INDEX_NAME}' created successfully.")
        else:
            print(f"Using existing Pinecone index: '{PINECONE_INDEX_NAME}'")

    except Exception as e:
        print(f"Error initializing Pinecone or creating index: {e}")
        sys.exit(1)

    print(f"Processing file: {args.file_path} of type: {args.content_type}")
    
    # Note: The current process_and_ingest_content is a placeholder.
    # You'll need to fully implement transcription, PDF parsing, embedding, and upserting.
    try:
        process_and_ingest_content(args.file_path, args.content_type)
        print("Ingestion process completed for the file.")
    except Exception as e:
        print(f"Error during content ingestion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # This script assumes that environment variables for OpenAI, Pinecone, etc., are set.
    # Example usage:
    # python scripts/ingest_data.py /path/to/your/week1_notes.pdf pdf
    # python scripts/ingest_data.py /path/to/your/week1_lecture.mp3 audio (once transcription is implemented)
    main()
