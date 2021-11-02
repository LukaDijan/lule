from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from starlette import status

API_KEY = "lule"
API_KEY_NAME = "Authorization"
api_key_header = APIKeyHeader(name=API_KEY_NAME)


async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(status.HTTP_403_FORBIDDEN)
