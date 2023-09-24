import datetime
import daiquiri
from fastapi import APIRouter, Request, Response


router = APIRouter()
log = daiquiri.getLogger(__name__)


@router.post('/v1/webhook')
@router.options('/v1/webhook')
async def manual_process(request: Request):
    print("chegou")
