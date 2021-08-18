from fastapi import FastAPI

from ..database.models import db


def get_app():
    app = FastAPI(title="lule API")
    db.init_app(app)
    return app


application = get_app()
