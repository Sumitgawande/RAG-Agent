from app.embeddings import embed
from app.llm import generate_answer

def retrieve(collection, query, company=None, year=None, top_k=5):
    query_embedding = embed([query])

    filters = []
    if company:
        filters.append(f'company == "{company}"')
    if year:
        filters.append(f"year == {year}")

    expr = " and ".join(filters) if filters else None

    results = collection.search(
        data=query_embedding,
        anns_field="embedding",
        param={"metric_type": "L2", "params": {"ef": 64}},
        limit=top_k,
        expr=expr,
        output_fields=["text", "company", "year"]
    )

    return results[0]

def answer_question(collection, question, company=None, year=None, use_llm=True):
    hits = retrieve(collection, question, company, year)

    texts = [hit.entity.get("text") for hit in hits]

    if not use_llm:
        return texts

    context = "\n".join(texts)
    return generate_answer(question, context)
