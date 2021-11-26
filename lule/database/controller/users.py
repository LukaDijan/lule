from typing import Optional
from uuid import UUID

from ...constants import UserRole
from ..models.user import User


async def get_student_by_email(email: str) -> Optional[User]:
    """Get student by email.

    Args:
        email (str): user email

    Returns:
        Optional[Student]: Student object if found, None otherwise
    """
    return await User.query.where(User.email == email).gino.first()


async def get_student_by_name(name: str) -> Optional[User]:
    return await User.query.where(User.name == name).gino.first()


async def store_student(
    id: UUID, name: str, email: str, role: UserRole
) -> User:
    return await User.create(id=id, name=name, email=email, role=role)


async def return_user(name) -> User:
    user = await User.query.where(User.name == name).gino.first()
    return user
