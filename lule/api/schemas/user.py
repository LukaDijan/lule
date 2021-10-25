from uuid import UUID

from pydantic import BaseModel, EmailStr

from ...constants import UserRole


class UserCreationRequest(BaseModel):
    name: str
    email: EmailStr
    role: UserRole = UserRole.STUDENT


class UserCreationResponse(BaseModel):
    user_id: UUID
