
from fastapi import FastAPI
from pydantic import BaseModel
from scraper import pesquisar

app = FastAPI(title="Boladas Scraper")

class Pesquisa(BaseModel):
    query: str

@app.get("/")
def home():
    return {"status": "online"}

@app.post("/search")
def search(data: Pesquisa):
    resultado = pesquisar(data.query)
    return resultado
