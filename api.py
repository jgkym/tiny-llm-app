from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Tiny LLM API")


# Define a data model for the input prompt
class Query(BaseModel):
    prompt: str


@app.post("/generate")
async def generate_text(query: Query):
    """
    Simulated endpoint to generate text.
    This is where you'd integrate your tiny LLM inference logic.
    """
    prompt = query.prompt
    # Here, a real model would process 'prompt
    # For now, we simulate a generated response
    response_text = f"Tiny LLM says: You wrote '{prompt}'. I'm still learning, so here's placeholder response."
    return {"response": response_text}


# Optional: Root endpoint to confirm API is running
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Tiny LLM API!"}
