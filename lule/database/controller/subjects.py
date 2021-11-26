from uuid import UUID

from lule.database.models.field import Field

from ..models.subject import Subject

"""
async def get_field_by_name(name: str) -> Optional[Field]:
    return await Field.query.where(Field.name == name).gino.first()
"""


async def store_subject(id: UUID, name: str) -> Field:
    return await Subject.create(id=id, name=name)


"""
async def return_user(name) -> User:
    user = await User.query.where(User.name == name).gino.first()
    return user
"""
