# RAG-Agent

# Financial Reports RAG System

This project implements a Retrieval-Augmented Generation (RAG) system for financial reports using SEC filings.

## Features
- Ingest large SEC filings into Milvus vector database.
- Generate embeddings using SentenceTransformer (`all-MiniLM-L6-v2`).
- Perform semantic search and answer queries via FastAPI.
- Supports large datasets with efficient chunking.

## Setup
1. Start Milvus services:

   docker-compose up -d

2. Place SEC filings in `data/2025q3/`.

3. Ingest data:

   python app/ingest.py

4. Run FastAPI server:

   uvicorn app.main:app --reload

## Notes
- Milvus collection: `financial_reports`
- Use Git LFS for files >100MB
- For large files, consider batching or GPU for faster embeddings.

