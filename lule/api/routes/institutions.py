from uuid import uuid4

from fastapi import APIRouter, Depends
from fastapi.security.api_key import APIKey

from ...database.controller.institutions import store_institution
from ..schemas.institutions import InstitutionCreationRequest
from ..security import get_api_key

router = APIRouter()


@router.post("/institutions", tags=["Institutions"])
async def create_institution(
    institution: InstitutionCreationRequest,
    api_key: APIKey = Depends(get_api_key),
):
    institution = await store_institution(
        uuid4(), institution.name, institution.country, institution.city
    )
    return {"institution_id": institution.id}
