import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get environment variables
EMBED_MODEL = os.getenv("OPENAI_EMBED_MODEL", "text-embedding-3-small")
CHAT_MODEL = os.getenv("OPENAI_CHAT_MODEL", "gpt-4.1-mini")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing from .env")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

print("Embedding Model:", EMBED_MODEL)
print("Chat Model:", CHAT_MODEL)


# Test 1: OpenAI Embeddings
embedding_response = client.embeddings.create(
    model=EMBED_MODEL,
    input="Hello OpenAI",
    dimensions=1024,
)

embedding_data = embedding_response.data[0].embedding

print("Embedding dimension:", len(embedding_data))


# Test 2: OpenAI Chat Model
chat_response = client.responses.create(
    model=CHAT_MODEL,
    input="Explain RAG in one sentence.",
    max_output_tokens=200,
)

print("OpenAI Response:", chat_response.output_text)
