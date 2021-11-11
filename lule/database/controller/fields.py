from typing import Optional

from ..models.field import Field


async def get_field_by_name(name: str) -> Optional[Field]:
    return await Field.query.where(Field.name == name).gino.first()
