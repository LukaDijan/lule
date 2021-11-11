from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security.api_key import APIKey

from ...database.controller.institutions import get_institution_by_name
from ...database.controller.programs import store_program
from ..schemas.programs import ProgramCreationRequest
from ..security import get_api_key

router = APIRouter(
    responses={
        404: {"description": "College with id '{institution_id}' not found."},
    }
)


@router.post("/institutions/{institution_id}/programs", tags=["Programs"])
async def create_program(
    program: ProgramCreationRequest, api_key: APIKey = Depends(get_api_key)
):
    if institution := await get_institution_by_name(program.institution):
        Program = await store_program(uuid4(), program.name, institution.id)
        # await Program.update(college_id = institution.id).apply()
        return {
            "inst_id": institution.id,
            "program_id": Program.id,
            "inst_name": institution.name,
            "program_name": Program.name,
        }
    raise HTTPException(
        status_code=404,
        detail="Institution doesn't exist",
    )
