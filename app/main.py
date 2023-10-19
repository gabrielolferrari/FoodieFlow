import uvicorn
import daiquiri
from fastapi import FastAPI, Request, Response

from application.commons.logging import configure as config_logging
from application.commons.response import make_response
from application.entrypoint import cliente_controller
from decouple import config

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

app.include_router(cliente_controller.router)

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
