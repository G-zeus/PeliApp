from fastapi import APIRouter, Query
from typing import Union
from ..controllers.movie import Movie

movies = APIRouter(prefix="/api/movies")
controller = Movie()


@movies.get("/popular")
def get_popular_movies(page: int | None = Query(gt=0, default=1)):
    return {"data": controller.get_popular(page=page)}


@movies.get("/find")
def get_popular_movies(search: Union[str]):
    return {"data": controller.search(search=search)}


@movies.get("/{id}")
def get_movie_detail(id: int):
    return {"data": controller.get_movie(id=id)}
