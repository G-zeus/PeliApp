from .routes.movies import movies
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config.config import get_settings

app = FastAPI()


def create_app():
    set_cors()
    get_routes()

    @app.get("/")
    def index():
        return {'msg': 'Api running', 'code': 200}

    return app


def get_routes():
    app.include_router(movies)


def set_cors():
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
