from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

openai.api_key = os.getenv("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")

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
