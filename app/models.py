from pydantic import BaseModel
from typing import Optional

class QuestionRequest(BaseModel):
    question: str
    company: Optional[str] = None
    year: Optional[int] = None
    use_llm: bool = True

class AnswerResponse(BaseModel):
    answer: str
