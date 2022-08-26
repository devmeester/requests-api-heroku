from fastapi import APIRouter

from api.v1.endpoints import requirement
from api.v1.endpoints import hardware
from api.v1.endpoints import user


api_router = APIRouter()
api_router.include_router(requirement.router, prefix='/requirements', tags=['requirements'])
api_router.include_router(hardware.router, prefix='/hardwares', tags=['hardwares'])
api_router.include_router(user.router, prefix='/users', tags=['users'])

