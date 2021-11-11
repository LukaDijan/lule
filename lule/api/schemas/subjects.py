from uuid import UUID

from pydantic import BaseModel


class SubjectCreationRequest(BaseModel):
    name: str


class SubjectCreationResponse(BaseModel):
    subject_id: UUID
