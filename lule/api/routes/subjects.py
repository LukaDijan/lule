from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security.api_key import APIKey

from ...database.controller.fields import get_field_by_name
from ...database.controller.institutions import get_institution_by_name
from ...database.controller.subjects import store_subject
from ..schemas.subjects import SubjectCreationRequest
from ..security import get_api_key

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
    instit_name: str,
    field_name: str,
    Subject: SubjectCreationRequest,
    api_key: APIKey = Depends(get_api_key),
):
    if institution := await get_institution_by_name(instit_name):
        if field := await get_field_by_name(field_name):
            await store_subject(uuid4(), Subject.name)
            return {"status": "success"}
    raise HTTPException(
        status_code=404,
        detail="Institution doesn't exist",
    )
