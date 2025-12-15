from app.milvus_db import connect_milvus, create_collection
from app.embeddings import embed

documents = [
    {
        "text": "Apple Inc reported Revenues of 394328000000 USD for fiscal year 2024.",
        "company": "Apple Inc",
        "year": 2024
    },
    {
        "text": "Microsoft Corp reported Revenues of 211915000000 USD for fiscal year 2024.",
        "company": "Microsoft Corp",
        "year": 2024
    }
]

connect_milvus()
collection = create_collection()

texts = [d["text"] for d in documents]
embeddings = embed(texts)

collection.insert([
    embeddings,
    [d["company"] for d in documents],
    [d["year"] for d in documents],
    texts
])

collection.flush()
