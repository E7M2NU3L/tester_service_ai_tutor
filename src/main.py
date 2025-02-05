from fastapi import FastAPI

# app instance
app = FastAPI()

# endpoints

# 1. /api/v1/tester-rag GET
@app.get("/api/v1/tester-rag")
def health_checker():
    return {"message": "Tester RAG health check successful"}

# 1. /api/v1/tester-rag/init POST
@app.post("/api/v1/tester-rag/init")
def init_tester_rag():
    return {"message": "Tester RAG initialization successful"}

# 2. /api/v1/tester-rag/eval POST
@app.post("/api/v1/tester-rag/eval")
def eval_tester_rag():
    return {"message": "Tester RAG evaluation successful"}