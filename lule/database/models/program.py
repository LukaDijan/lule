from sqlalchemy.dialects.postgresql import UUID

from .base import db


class Program(db.Model):
    __tablename__ = "programs"

    id = db.Column(UUID, primary_key=True)
    name = db.Column(db.String(), nullable=True)
    college_id = db.Column(UUID, db.ForeignKey("institutions.id"))
