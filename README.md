# ❤️‍🔥 Chatbot API experto en el Cúcuta Deportivo

Este proyecto es una API REST construida con **FastAPI** que simula un chatbot especializado únicamente en el **Cúcuta Deportivo**, equipo profesional del fútbol colombiano. Usa el modelo **Mistral** a través de la plataforma **OpenRouter**, que es compatible con la API de OpenAI.

Ideal para aficionados que quieran saber más sobre la historia, jugadores, títulos, comunas, cánticos, parches, campañas destacadas y demás curiosidades del glorioso Cúcuta Deportivo.

---

## 🚀 Requisitos

- Python 3.8 o superior
- Tener una API Key válida de OpenRouter
- Conexión a internet
- Opcional: Docker y cuenta en Render para despliegue

---

## 🛠 Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu_usuario/chatbot-cucuta.git
   cd chatbot-cucuta
Crea el entorno virtual:

bash
Copiar
Editar
python -m venv venv
Activa el entorno:

En Windows:

bash
Copiar
Editar
venv\Scripts\activate
En macOS/Linux:

bash
Copiar
Editar
source venv/bin/activate
Instala las dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Crea un archivo .env en la raíz del proyecto con el siguiente contenido:

env
Copiar
Editar
API_KEY=tu_api_key_de_openrouter
BASE_URL=https://openrouter.ai/api/v1
▶ Ejecución local
Inicia el servidor local con:

bash
Copiar
Editar
uvicorn main:app --reload
Documentación Swagger: http://127.0.0.1:8000/docs

Documentación Redoc: http://127.0.0.1:8000/redoc

Endpoint principal: /chat (método POST)

📬 Ejemplo de uso
Petición (POST a /chat):

json
Copiar
Editar
{
  "pregunta": "¿Quién fue el arquero del Cúcuta en 2006?"
}
Respuesta esperada:

json
Copiar
Editar
{
  "respuesta": "En el 2006, el arquero titular del Cúcuta Deportivo fue Robinson Zapata. Fue una pieza clave para lograr el campeonato en el Torneo Finalización."
}
🐳 Despliegue con Docker
Construye la imagen:

bash
Copiar
Editar
docker build -t cucuta-chatbot .
Ejecuta el contenedor:

bash
Copiar
Editar
docker run -d -p 8000:8000 --env-file .env cucuta-chatbot
☁️ Despliegue en Render
Crea un nuevo servicio Web Service en https://render.com

Conecta tu repositorio de GitHub

Agrega las variables de entorno desde .env

Usa este comando como Start Command:

bash
Copiar
Editar
uvicorn main:app --host 0.0.0.0 --port 8000
📁 Estructura del Proyecto
bash
Copiar
Editar
chatbot-cucuta/
├── main.py           # Lógica principal de la API
├── config.py         # PROMPT del sistema y configuraciones
├── .env              # Variables sensibles (no subir al repo)
├── requirements.txt  # Dependencias del proyecto
├── Dockerfile        # Imagen para contenedor
└── README.md         # Este archivo
⚽ Conocimiento del Chatbot
El chatbot está entrenado para responder preguntas sobre:

Historia y títulos del Cúcuta Deportivo

Plantillas históricas y jugadores destacados

Hinchada, cánticos, parches y comunas

Rivalidades y momentos históricos

Estadísticas del club y ascensos/descensos

Cultura futbolera cucuteña (CD, LBI, AGT, Norte, etc.)

💬 También entiende términos usados por la hinchada como:
“agt”, “comunas”, “CD”, “LBI”, “parches”, entre otros.


## 👨‍💻 Autor del codigo base
Ing. Cristian Díaz <p align="center">
  <img width="80" src="https://i.imgur.com/YYf2LgH.png">
</p>

## 👨‍💻 Creacion del Frontend y Modificaciones

Est. **Yantrresky Alveiro Rivera Martinez**
