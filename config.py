import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI") or "mongodb://localhost:27017/enertech"
    SECRET_KEY = os.getenv("SECRET_KEY") or "clave_por_defecto_segura"
