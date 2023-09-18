from .routes.movies import movies
from fastapi import FastAPI
from .config.config import get_settings

app = FastAPI()


def create_app():
    get_routes()

    @app.get("/")
    def index():
        return {'msg': 'Api running', 'code': 200}

    return app


def get_routes():
    app.include_router(movies)
