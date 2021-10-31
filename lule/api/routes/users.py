from uuid import uuid4

from fastapi import APIRouter, HTTPException, status

from ...database.controller.users import get_student_by_email, store_student
from ..schemas.user import UserCreationRequest

router = APIRouter()


@router.post("/users", tags=["User"])
async def create_user(user: UserCreationRequest):
    if await get_student_by_email(user.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Email already exists"
        )

    student = await store_student(uuid4(), user.name, user.email, user.role)

    return {"user_id": student.id}
