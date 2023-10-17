import uvicorn
from fastapi import FastAPI, Request, Response

from commons.logging import configure as config_logging
from commons.response import make_response
from routes import produtos
from decouple import config

HOST = config('HOST', default='127.0.0.1')
PORT = config('PORT', default='8000')

config_logging()

app = FastAPI()

app.router.redirect_slashes = False

# register routes
app.include_router(produtos.router)


@app.get('/healthcheck')
@app.options('/healthcheck')
async def healthcheck(request: Request) -> Response:
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
