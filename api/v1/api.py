from fastapi import APIRouter

from api.v1.endpoints import requirement
from api.v1.endpoints import hardware


api_router = APIRouter()
api_router.include_router(requirement.router, prefix='/requirements', tags=['requirements'])
api_router.include_router(hardware.router, prefix='/hardwares', tags=['hardwares'])

