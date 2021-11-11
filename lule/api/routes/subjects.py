from uuid import uuid4

from fastapi import APIRouter, HTTPException

from ...database.controller.fields import get_field_by_name
from ...database.controller.institutions import get_institution_by_name
from ...database.controller.subjects import store_subject
from ..schemas.subjects import SubjectCreationRequest

router = APIRouter(
    responses={
        404: {"description": "Subject with id '{subject_id}' not found."},
    }
)


@router.post(
    "/institutions/{institution_id}/programs/{program_id}/subjects",
    tags=["Subjects"],
)
async def create_subject(
    instit_name: str, field_name: str, Subject: SubjectCreationRequest
):
    if institution := await get_institution_by_name(instit_name):
        if field := await get_field_by_name(field_name):
            await store_subject(uuid4(), Subject.name)
            return {"status": "success"}
    raise HTTPException(
        status_code=404,
        detail="Institution doesn't exist",
    )
