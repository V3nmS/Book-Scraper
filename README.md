# BOOK-SCRAPER

## Lo que voy a construir

Una CLI que recorre todo el catálogo de books.toscrape.com (sitio hehco para practicar spcraping, cero problemas legales) y entrega un archivo con título, precio, rating disponibilidad, categoría y URL de cada libro.

# Cuándo está hecho:

- `pyhton scraper.py --output books.xlsx` books.xlsx saca los ~1000 libros recorriendo la paginación.
- `--format csv|xlsx` y `--max-pages N` funcionan.
- Si una página falla, reintenta con espera y no truena.
- Hay pausa entre requests, porque los clientes preguntan por eso.
- Trae requierements.txt y un README con qué hace, cómo se instala, cómo se corre y una captura del Excel resultante.
