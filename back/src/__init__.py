from fastapi import FastAPI

app = FastAPI()


def create_app():

    @app.get("/")
    def index():
        return {'msg': 'Api running', 'code': 200}

    return app

