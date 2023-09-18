from fastapi import APIRouter
from typing import Union
from ..controllers.movie import Movie

movies = APIRouter(prefix="/api/movies")
controller = Movie()


@movies.get("/popular")
def get_popular_movies(page: Union[int, None] = None):
    return {"data": controller.get_popular(page=page)}


@movies.get("/{id}")
def get_movie_detail(id: int):
    return {"_id": id}
