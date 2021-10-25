from fastapi import FastAPI

from ..database.models import db
from .routes import users


def get_app():
    app = FastAPI(title="lule API")
    db.init_app(app)
    return app


application = get_app()

application.include_router(users.router)
