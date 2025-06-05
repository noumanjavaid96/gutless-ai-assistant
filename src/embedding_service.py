# src/embedding_service.py
import os
import openai

# Ensure your OpenAI API key is set as an environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

EMBEDDING_MODEL = "text-embedding-ada-002"

def get_embedding(text: str, model: str = EMBEDDING_MODEL) -> list[float]:
    """Generates an embedding for the given text using OpenAI's API."""
    if not text or not isinstance(text, str):
        raise ValueError("Input text must be a non-empty string.")
    
    try:
        text = text.replace("\n", " ") # Replace newlines with spaces, as per OpenAI's recommendation
        response = openai.Embedding.create(input=[text], model=model)
        return response['data'][0]['embedding']
    except Exception as e:
        print(f"Error generating embedding: {e}")
        # Potentially re-raise or handle more gracefully
        raise

if __name__ == '__main__':
    if not openai.api_key:
        print("OPENAI_API_KEY environment variable not set. Please set it to test embeddings.")
    else:
        sample_text = "This is a test sentence for generating embeddings."
        try:
            embedding = get_embedding(sample_text)
            print(f"Generated embedding for: '{sample_text}'")
            print(f"Embedding vector (first 5 dimensions): {embedding[:5]}")
            print(f"Embedding dimension: {len(embedding)}")
        except Exception as e:
            print(f"Failed to generate embedding: {e}")
