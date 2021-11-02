from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from starlette import status

from .env import API_KEY, API_KEY_NAME

api_key_header = APIKeyHeader(name=API_KEY_NAME)


async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)
