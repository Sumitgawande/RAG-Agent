from fastapi import FastAPI
from app.milvus_db import connect_milvus, create_collection
from app.rag import answer_question
from app.models import QuestionRequest, AnswerResponse

app = FastAPI(title="Financial RAG API")

connect_milvus()
collection = create_collection()

@app.post("/ask", response_model=AnswerResponse)
def ask_question(req: QuestionRequest):
    answer = answer_question(
        collection=collection,
        question=req.question,
        company=req.company,
        year=req.year,
        use_llm=req.use_llm
    )

    if isinstance(answer, list):
        answer = " ".join(answer)

    return AnswerResponse(answer=answer)
