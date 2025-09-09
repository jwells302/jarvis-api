from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class CommandRequest(BaseModel):
    command: str

@app.post("/ask")
async def ask_jarvis(request: CommandRequest):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are JARVIS, a helpful AI assistant."},
            {"role": "user", "content": request.command}
        ]
    )
    reply = response.choices[0].message["content"]
    return {"reply": reply}
