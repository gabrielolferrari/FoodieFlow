import uvicorn
from fastapi import FastAPI, Request, Response

from app.commons.logging import configure as config_logging
from commons.response import make_response
from routes import EXEMPLOROTA



config_logging()

app = FastAPI()

app.router.redirect_slashes = False

# register routes
app.include_router(EXEMPLOROTA.router)


@app.get('/')
@app.options('/')
async def index() -> Response:
    return Response(status_code=200)


@app.get('/healthcheck')
@app.options('/healthcheck')
async def healthcheck(request: Request) -> Response:
    return make_response(request=request, body={'status': 'UP'}, status_code=200)


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='127.0.0.1',
        port=8000,
        reload=True,
        workers=1,
        server_header=False,
        access_log=False,
    )
