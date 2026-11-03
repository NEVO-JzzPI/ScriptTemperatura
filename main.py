import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from generador import generar_datos
import estado

app = FastAPI()

#Es el sensor simulado corriendo en loop infinito
async def generar_periodicamente():
    while True:
        estado.ultima_lectura = generar_datos()
        await asyncio.sleep(estado.intervalo_segundos)
        
#gestor de ciclo de vida: código que corre al arrancar y al apagar el servido
@asynccontextmanager
async def lifespan(app: FastAPI):
    tarea = asyncio.create_task(generar_periodicamente())
    yield
    tarea.cancel()

app = FastAPI(lifespan=lifespan)

@app.get("/datos")
def obtener_datos():
    return estado.ultima_lectura

@app.put("/config/intervalo")
def cambiar_intervalo(segundos: int):
    if not (1 <= segundos <= 60):
        return {"error": "El intervalo debe estar entre 1 y 60 segundos"}
    estado.intervalo_segundos = segundos
    return {"intervalo_segundos": estado.intervalo_segundos}