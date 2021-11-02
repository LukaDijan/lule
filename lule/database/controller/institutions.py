from uuid import UUID

from ..models.institution import Institution


async def store_institution(
    id: UUID, name: str, country: str, city: str
) -> Institution:
    return await Institution.create(
        id=id, name=name, country=country, city=city
    )
