from uuid import uuid4

from fastapi import APIRouter

from ...database.controller.institutions import store_institution
from ..schemas.institutions import InstitutionCreationRequest

router = APIRouter()


@router.post("/institutions", tags=["Institutions"])
async def create_institution(institution: InstitutionCreationRequest):
    institution = await store_institution(
        uuid4(), institution.name, institution.country, institution.city
    )
    return {institution.id}
