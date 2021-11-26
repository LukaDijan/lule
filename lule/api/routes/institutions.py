from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security.api_key import APIKey

from ...database.controller.institutions import (
    get_institution_by_name,
    store_institution,
)
from ..schemas.institutions import InstitutionCreationRequest
from ..security import get_api_key

router = APIRouter(
    responses={
        404: {"description": "College with id '{institution_id}' not found."},
    }
)


@router.post("/institutions", tags=["Institutions"])
async def create_institution(
    institution: InstitutionCreationRequest,
    api_key: APIKey = Depends(get_api_key),
):
    institution = await store_institution(
        uuid4(), institution.name, institution.country, institution.city
    )
    return {"institution_id": institution.id}


@router.get("/institutions/{institution_id}", tags=["Institutions"])
async def return_institution(
    name: str, api_key: APIKey = Depends(get_api_key)
):
    if institution := await get_institution_by_name(name):
        return {
            "institution_id": institution.id,
            "institution_name": institution.name,
            "institution_country": institution.country,
            "institution_city": institution.city,
        }
    raise HTTPException(
        status_code=404,
        detail="Institution doesn't exist",
    )
