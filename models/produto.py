from pydantic import BaseModel

class Produto(BaseModel):
    titulo: str
    preco: str
    cidade: str
    imagem: str
    link: str
    fonte: str
