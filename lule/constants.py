import enum


@enum.unique
class UserRole(str, enum.Enum):
    ADMINISTATOR = "administrator"
    STUDENT = "student"
