from pinecone import Pinecone
from dotenv import load_dotenv
import os
import random

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index(os.getenv("PINECONE_INDEX_NAME"))


def batch_upsert(chunks: list, embeddings: list, batch_limit: int = 100):
    chunks_length = len(chunks)
    iters = chunks_length // batch_limit + (chunks_length % batch_limit > 0)

    print(f"Process has begun with {iters} batches.")

    for i in range(iters):
        start = i * batch_limit
        end = min((i + 1) * batch_limit, chunks_length)

        batch = []
        for j in range(start, end):
            vector_id = str(random.randint(1, 1e9))
            vector = {
                "id": vector_id,
                "values": embeddings[j],
                "metadata": {"chunk": chunks[j]}
            }
            batch.append(vector)

        index.upsert(vectors=batch)
        print(f"Batch {i + 1}/{iters} uploaded.")

    print("All batches have been successfully uploaded.")
