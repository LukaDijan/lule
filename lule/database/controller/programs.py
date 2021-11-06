from uuid import UUID

from ..models.field import Field


async def store_program(id: UUID, name: str, college_id: UUID) -> Field:
    return await Field.create(id=id, name=name, college_id=college_id)
