from sentence_transformers import SentenceTransformer

MISTRAL_API_KEY = "z0IT92lT374zXuRhWjg2agXtcgMs2T0j"
MISTRAL_API_BASE = "https://api.mistral.ai/v1"
# MISTRAL_API_BASE = "http://localhost:11434/api"
GITHUB_REPO = "jacko773/javaquiz"
EMBEDDING_MODEL_NAME = "BAAI/bge-m3"


headers = {
    "Authorization": f"Bearer {MISTRAL_API_KEY}",
    "Content-Type": "application/json",
}

# Load the BGE-M3 embedding model
embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)