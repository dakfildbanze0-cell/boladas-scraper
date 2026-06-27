```python
from .base import BaseScraper

class OLXScraper(BaseScraper):

    def search(self, query: str):
        # por enquanto simulação (depois vira scraping real)
        return [
            {
                "titulo": f"{query} - OLX anúncio 1",
                "preco": "35000 MT",
                "cidade": "Maputo",
                "imagem": "",
                "link": "https://olx.co.mz/exemplo1",
                "fonte": "OLX"
            }
        ]
```
