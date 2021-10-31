from sqlalchemy.dialects.postgresql import UUID

from .base import db


class InstitutionField(db.Model):
    __tablename__ = "institution_field"

    college_id = db.Column(UUID, db.ForeignKey("institutions.id"))
    field_id = db.Column(UUID, db.ForeignKey("fields.id"))
