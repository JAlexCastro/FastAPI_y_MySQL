#Package FastAPI
from fastapi import FastAPI

#Modulo Interno
from routes.user import user

app = FastAPI()     #Para Ejecutar, CMD: uvicorn app:app --reload

app.include_router(user)

