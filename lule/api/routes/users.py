from uuid import uuid4

from fastapi import APIRouter, HTTPException

from ...database.controller.institutions import get_institution_by_name
from ...database.controller.users import (
    get_student_by_email,
    get_student_by_name,
    store_student,
)
from ..schemas.user import UserCreationRequest

router = APIRouter(
    responses={
        404: {"description": "User ne postoji"},
        409: {"description": "User s istim mailom vec registriran"},
    }
)


@router.post("/users", tags=["User"])
async def create_user(user: UserCreationRequest):
    if await get_student_by_email(user.email):
        raise HTTPException(status_code=409, detail="Email already exists")

    student = await store_student(uuid4(), user.name, user.email, user.role)

    return {"user_id": student.id}


@router.get("/users/{username}", tags=["User"])
async def read_user(username: str):
    if user := await get_student_by_name(username):
        return {"user_name": user.name, "user_email": user.email}
    raise HTTPException(status_code=408, detail="User does not exist")


@router.patch("/users/{user_id}", tags=["User"])
async def add_inst(email: str, inst_name: str):
    if student := await get_student_by_email(email):
        if institution := await get_institution_by_name(inst_name):
            await student.update(institution_id=institution.id).apply()
            return {"status": "success"}

        raise HTTPException(
            status_code=404, detail="Institution doesn't exist"
        )

    raise HTTPException(status_code=404, detail="User doesn't exist")
