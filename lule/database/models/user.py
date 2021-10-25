from sqlalchemy.dialects.postgresql import UUID

from .base import db


class User(db.Model):
    __tablename__ = "students"

    id = db.Column(UUID, primary_key=True)
    name = db.Column(db.String(), nullable=True)
    email = db.Column(db.String(), nullable=True, unique=True)
    role = db.Column(db.String())
    subjects = db.Column(db.String(), nullable=True)
    institution_id = db.Column(
        UUID, db.ForeignKey("institutions.id"), nullable=True
    )
