import requests
from dotenv import load_dotenv
import os

load_dotenv()


def segmenter(text: str) -> list:
    url = 'https://segment.jina.ai/'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {os.getenv("JINA_API_KEY")}'
    }
    data = {
        "content": text,
        "return_chunks": True,
        "max_chunk_length": 1000
    }

    response = requests.post(url, headers=headers, json=data)
    return list(response.json()['chunks'])
