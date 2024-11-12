import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()


def generate_embeddings(chunks: list,  dimensions: int = 512, late_chunking: bool = False) -> list:
    data = json.dumps({
        "model": "jina-embeddings-v3",
        "task": "text-matching",
        "dimensions": dimensions,
        "late_chunking": late_chunking,
        "embedding_type": "float",
        "input": chunks
    })

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('JINA_API_KEY')}"
    }

    response = requests.post(
        "https://api.jina.ai/v1/embeddings", headers=headers, data=data)

    return [chunk['embedding'] for chunk in response.json()['data']]
