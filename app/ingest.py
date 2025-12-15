# import os
# from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility
# from sentence_transformers import SentenceTransformer

# # -----------------------------
# # 1. Connect to Milvus
# # -----------------------------
# connections.connect(alias="default", host="localhost", port="19530")
# print("✅ Connected to Milvus")

# # -----------------------------
# # 2. Create or get collection
# # -----------------------------
# collection_name = "financial_reports"

# # ✅ Correct check for existing collection
# if collection_name in utility.list_collections():
#     collection = Collection(collection_name)
#     print(f"Collection '{collection_name}' already exists")
# else:
#     fields = [
#         FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
#         FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384),
#         FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=65535)
#     ]
#     schema = CollectionSchema(fields, description="2025 Q3 Financial Reports")
#     collection = Collection(collection_name, schema)
#     print(f"Collection '{collection_name}' created")

# # -----------------------------
# # 3. Load embedding model
# # -----------------------------
# model = SentenceTransformer('all-MiniLM-L6-v2')
# print("✅ Embedding model loaded")

# # -----------------------------
# # 4. Path to your data folder
# # -----------------------------

# data_folder = os.path.join(os.path.dirname(__file__), '..', 'data', '2025q3')
# data_folder = os.path.abspath(data_folder)  # convert to absolute path
# print("Reading files from:", data_folder)
# # data_folder = "../data/2025q3" 


# # -----------------------------
# # 5. Process and ingest all files
# # -----------------------------
# for filename in os.listdir(data_folder):
#     if filename.endswith(".txt"):
#         filepath = os.path.join(data_folder, filename)
#         with open(filepath, 'r', encoding='utf-8') as f:
#             text = f.read()

#         # Split text into chunks (500 characters each)
#         chunks = [text[i:i+500] for i in range(0, len(text), 500)]

#         # Generate embeddings
#         embeddings = model.encode(chunks).tolist()

#         # Insert into Milvus
#         collection.insert([
#             list(range(len(chunks))),  # ignored if auto_id=True
#             embeddings,
#             chunks
#         ])
#         print(f"Ingested {len(chunks)} chunks from {filename}")

# print("✅ All files ingested successfully!")

from pymilvus import connections, utility

# Connect to Milvus
connections.connect(alias="default", host="localhost", port="19530")

collection_name = "financial_reports"

# Check if collection exists
if collection_name in utility.list_collections():
    utility.drop_collection(collection_name)
    print(f"Collection '{collection_name}' dropped successfully.")
else:
    print(f"Collection '{collection_name}' does not exist.")

