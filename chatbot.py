from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from openai import OpenAI
from config import PROMPT_SISTEMA
from dotenv import load_dotenv
import os
import asyncio

# --- CARGAR VARIABLES .env ---
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
if not API_KEY:
    print("⚠️ ADVERTENCIA: No se encontró API_KEY en .env")

# --- CLIENTE OPENAI ---
client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL  # ej: "https://api.groq.com/openai/v1"
)

# --- FASTAPI ---
app = FastAPI()

# --- CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Cambiar a tu dominio en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MODELO PARA PETICIONES ---
class Pregunta(BaseModel):
    pregunta: str


# ============================================================
# 🚀 RUTA POST PARA RESPUESTA NORMAL (SIN STREAMING)
# ============================================================
@app.post("/chat")
async def obtener_respuesta(data: Pregunta):
    try:
        respuesta = client.chat.completions.create(
            model="gpt-4o-mini",  # Cambia al modelo que estés usando
            messages=[
                {"role": "system", "content": PROMPT_SISTEMA},
                {"role": "user", "content": data.pregunta}
            ]
        )

        return {"respuesta": respuesta.choices[0].message["content"]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================
# 🚀 RUTA PARA STREAMING (OPCIONAL)
# ============================================================
@app.post("/stream")
async def chat_stream(data: Pregunta):

    def generador():
        try:
            respuesta = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": PROMPT_SISTEMA},
                    {"role": "user", "content": data.pregunta}
                ],
                stream=True
            )

            for parte in respuesta:
                texto = parte.choices[0].delta.get("content", "")
                if texto:
                    yield texto

        except Exception as e:
            yield f"[Error]: {str(e)}"

    return StreamingResponse(generador(), media_type="text/plain")
