from pymilvus import (
    connections, FieldSchema, CollectionSchema,
    DataType, Collection
)

COLLECTION_NAME = "sec_rag"

def connect_milvus():
    connections.connect(
        alias="default",
        host="localhost",
        port="19530"
    )

def create_collection():
    fields = [
        FieldSchema(
            name="id",
            dtype=DataType.INT64,
            is_primary=True,
            auto_id=True
        ),
        FieldSchema(
            name="embedding",
            dtype=DataType.FLOAT_VECTOR,
            dim=384
        ),
        FieldSchema(
            name="company",
            dtype=DataType.VARCHAR,
            max_length=100
        ),
        FieldSchema(
            name="year",
            dtype=DataType.INT64
        ),
        FieldSchema(
            name="text",
            dtype=DataType.VARCHAR,
            max_length=1024
        )
    ]

    schema = CollectionSchema(fields, "SEC Financial RAG")
    collection = Collection(COLLECTION_NAME, schema)

    collection.create_index(
        field_name="embedding",
        index_params={
            "index_type": "HNSW",
            "metric_type": "L2",
            "params": {"M": 8, "efConstruction": 64}
        }
    )

    collection.load()
    return collection
