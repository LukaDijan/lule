from uuid import UUID

from pydantic import BaseModel


class InstitutionCreationRequest(BaseModel):
    name: str
    country: str
    city: str


class InstitutionCreationResponse(BaseModel):
    institution_id: UUID
