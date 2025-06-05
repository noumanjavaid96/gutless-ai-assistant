# src/pinecone_service.py
import os
import pinecone

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.environ.get("PINECONE_ENVIRONMENT")
PINECONE_INDEX_NAME = os.environ.get("PINECONE_INDEX_NAME", "gutless-ai-assistant")

_pinecone_index = None

def initialize_pinecone():
    """Initializes connection to Pinecone and gets the index."""
    global _pinecone_index
    if not PINECONE_API_KEY or not PINECONE_ENVIRONMENT:
        raise ValueError("PINECONE_API_KEY and PINECONE_ENVIRONMENT must be set in environment variables.")
    
    pinecone.init(
        api_key=PINECONE_API_KEY,
        environment=PINECONE_ENVIRONMENT
    )
    
    if PINECONE_INDEX_NAME not in pinecone.list_indexes():
        # For POC, we might create it if it doesn't exist. 
        # For production, this should be handled carefully.
        # pinecone.create_index(PINECONE_INDEX_NAME, dimension=1536) # Assuming OpenAI's ada-002 dimension
        # print(f"Pinecone index '{PINECONE_INDEX_NAME}' created.")
        # For now, let's assume it must exist or raise an error for the bot to function.
        raise EnvironmentError(f"Pinecone index '{PINECONE_INDEX_NAME}' does not exist. Please create it.")
        
    _pinecone_index = pinecone.Index(PINECONE_INDEX_NAME)
    print(f"Successfully connected to Pinecone index: '{PINECONE_INDEX_NAME}'")
    return _pinecone_index

def get_pinecone_index():
    """Returns the initialized Pinecone index. Initializes if not already done."""
    if _pinecone_index is None:
        return initialize_pinecone()
    return _pinecone_index

def upsert_to_pinecone(vectors: list, index_name: str = None):
    """
    Upserts vectors to the specified Pinecone index.
    Vectors should be a list of tuples: (id, vector, metadata_dict)
    e.g., [('vec1', [0.1, 0.2, ...], {'text': 'some text', 'source': 'doc1'})]
    """
    idx = get_pinecone_index()
    # target_index_name = index_name or PINECONE_INDEX_NAME
    # idx = pinecone.Index(target_index_name)
    upsert_response = idx.upsert(vectors=vectors)
    print(f"Upserted {len(vectors)} vectors. Response: {upsert_response}")
    return upsert_response

def query_pinecone(query_vector: list[float], top_k: int = 5, index_name: str = None) -> list:
    """Queries the Pinecone index with the given vector."""
    idx = get_pinecone_index()
    # target_index_name = index_name or PINECONE_INDEX_NAME
    # idx = pinecone.Index(target_index_name)
    query_results = idx.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True
    )
    # print(f"Query results: {query_results}")
    return query_results.get('matches', [])

if __name__ == '__main__':
    # This basic test assumes the index exists and env vars are set.
    # For a real test, you'd mock Pinecone or have a test index.
    try:
        print("Attempting to initialize Pinecone...")
        index = initialize_pinecone()
        print(f"Pinecone initialized. Index stats: {index.describe_index_stats()}")
        
        # Example: Try a dummy query (will likely return nothing or error if index is empty/wrong dimension)
        # dummy_vector = [0.0] * 1536 # Dimension for text-embedding-ada-002
        # print("\nAttempting a dummy query...")
        # results = query_pinecone(dummy_vector, top_k=1)
        # print(f"Dummy query results: {results}")

    except Exception as e:
        print(f"Error during Pinecone service test: {e}")
        print("Ensure PINECONE_API_KEY, PINECONE_ENVIRONMENT, and PINECONE_INDEX_NAME are set correctly,")
        print(f"and the index '{PINECONE_INDEX_NAME or 'gutless-ai-assistant'}' exists in environment '{PINECONE_ENVIRONMENT}'.")

