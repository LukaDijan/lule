from sqlalchemy.dialects.postgresql import UUID

from .base import db


class College(db.Model):
    __tablename__ = "colleges"

    id = db.Column(UUID, primary_key=True)
    name = db.Column(db.String(), nullable=True)
    semester = db.Column(db.String(), nullable=True)
