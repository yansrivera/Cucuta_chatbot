from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from openai import OpenAI
from config import PROMPT_SISTEMA
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

app = FastAPI()

# --- HABILITAR CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción cambia esto a tu dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Pregunta(BaseModel):
    pregunta: str

@app.post("/chat")
async def obtener_respuesta(p: Pregunta):
    try:
        # Streaming desde la API
        stream = client.chat.completions.create(
            model="mistralai/mistral-small-3.1-24b-instruct:free",
            messages=[
                {"role": "system", "content": PROMPT_SISTEMA},
                {"role": "user", "content": p.pregunta}
            ],
            stream=True
        )

        def generar():
            for chunk in stream:
                if chunk.choices[0].delta and chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content

        return StreamingResponse(generar(), media_type="text/plain")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
