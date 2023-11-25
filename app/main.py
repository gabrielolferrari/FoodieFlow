import uvicorn
import daiquiri
from fastapi import FastAPI, Request, Response

from application.commons.logging import configure as config_logging
from application.commons.response import make_response
from decouple import config
from infrastructure.database import init_db;
from application.entrypoint import cliente_controller
from application.entrypoint import categoria_controller
from application.entrypoint import produto_controller
from application.entrypoint import pedido_controller
from core.model.orm import status, cliente, categoria, imagem, ingrediente, produto, pedido



HOST = config('HOST_API', default='localhost')
PORT = config('PORT_API', default='8000')

config_logging()

log = daiquiri.getLogger(__name__)

app = FastAPI(
    title='Foodie Flow',
    description='API - Tech Challenge - FIAP',
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redocs',
)

app.router.redirect_slashes = True

app.include_router(cliente_controller.router, prefix='/clientes')
app.include_router(categoria_controller.router, prefix='/categorias')
app.include_router(produto_controller.router, prefix='/produtos')
app.include_router(pedido_controller.router, prefix='/pedidos')

@app.on_event("startup")
async def startup_event():
    init_db()

@app.get('/healthcheck', description='Healthcheck da API')
@app.options('/healthcheck', description='Healthcheck da API')
async def healthcheck(request: Request) -> Response:
    log.info(f'Healthcheck solicitado')
    return make_response(request=request, body={'status': 'UP'}, status_code=200)


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=HOST,
        port=PORT,
        reload=True,
        workers=1,
        server_header=False,
        access_log=False,
    )
