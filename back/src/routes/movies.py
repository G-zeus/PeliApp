from fastapi import APIRouter
from typing import Union

movies = APIRouter(prefix="/api/movies")


@movies.get("/popular")
def get_popular_movies(page: Union[int, None] = None):
    return {"data": {"page": page, "movies": ""}}


@movies.get("/{id}")
def get_movie_detail(id: int):
    return {"_id": id}
