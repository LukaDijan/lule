from uuid import UUID

from pydantic import BaseModel


class ProgramCreationRequest(BaseModel):
    name: str
    institution: str


class ProgramCreationResponse(BaseModel):
    program_id: UUID
