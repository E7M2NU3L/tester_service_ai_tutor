from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from src import utils

# app instance
app = FastAPI()

# Types for test initialization and evaluation

# 1. input types - initialization of the tester
class CreateTestProps(BaseModel):
    pass_marks: int
    total_marks: int
    test_count: int
    documents: List[str]
    urls: List[str]

    class Config:
        arbitrary_types_allowed = True

# 2. input types - Test Evaluation Types
class Question(BaseModel):
    question: str
    options: List[str]
    answer: str

class TestEvaluationProps(BaseModel):
    questions: List[Question]
    db_path: str

# 3. output types - Test Evaluation Types
class TestResultProps(BaseModel):
    question: str
    db_path: str
    options: List[str]
    answer: str
    marks: int
    feedback: str

# 4. Output types - Test Initialization Types
class QuestionForInit(BaseModel):
    question: str
    options: List[str]
    total_marks: int

class Quizzes(BaseModel):
    test_count: int
    pass_marks: int
    total_marks: int
    title: str
    description: str
    questions: List[QuestionForInit]

class TestInitializationResultProps(BaseModel):
    quizzes: List[Quizzes]
    pass_mark: int
    total_mark: int
    test_count: int
    db_path: str

# Endpoints

# 1. /api/v1/tester-rag GET
@app.get("/api/v1/tester-rag")
def health_checker():
    return {"message": "Tester RAG health check successful"}

# 2. /api/v1/tester-rag/init POST
@app.post("/api/v1/tester-rag/init", response_model=TestInitializationResultProps)
def init_tester_rag(test: CreateTestProps):
    contextInstance = utils.GenerateOutput()
    context = contextInstance.generate_output()
    return context

# 3. /api/v1/tester-rag/eval POST
@app.post("/api/v1/tester-rag/eval", response_model=List[TestResultProps])
def eval_tester_rag(evaluate: TestEvaluationProps):
    # Include logic to evaluate the test
    return [{
        "question": question.question,
        "db_path": evaluate.db_path,
        "options": question.options,
        "answer": question.answer,
        "marks": 0,  # Logic for marks should be here
        "feedback": "Correct/Incorrect"  # Logic for feedback
    } for question in evaluate.questions]