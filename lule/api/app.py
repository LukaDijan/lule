from fastapi import FastAPI

from ..database.models import db
from .routes import institutions, users


def get_app():
    app = FastAPI(title="lule API")
    db.init_app(app)
    return app


application = get_app()

application.include_router(users.router)
application.include_router(institutions.router)
