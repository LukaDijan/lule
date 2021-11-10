from sqlalchemy.dialects.postgresql import UUID

from .base import db


class Subject(db.Model):
    __tablename__ = "subjects"

    id = db.Column(UUID, primary_key=True)
    name = db.Column(db.String(), nullable=True)
    field = db.Column(UUID, db.ForeignKey("field.id"), nullable=True)
