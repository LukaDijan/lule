from sqlalchemy.dialects.postgresql import UUID

from .base import db


class Institution(db.Model):
    __tablename__ = "institutions"

    id = db.Column(UUID, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    country = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(), nullable=False)
