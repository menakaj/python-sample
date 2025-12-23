from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    session_id: str = None

class ChatResponse(BaseModel):
    response: str
    session_id: str = None

@app.post("/chat")
async def chat(request: ChatRequest):
    # Simple echo response - replace with your actual logic
    response_text = f"You said: {request.message}"

    return ChatResponse(
        response=response_text,
        session_id=request.session_id
    )

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    print("Starting chat API server on http://0.0.0.0:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
