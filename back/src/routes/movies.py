from fastapi import APIRouter, Query
from ..controllers.movie import Movie

movies = APIRouter(prefix="/api/movies")
controller = Movie()


@movies.get("/popular")
def get_popular_movies(page: int | None = Query(gt=0)):
    return {"data": controller.get_popular(page=page)}


@movies.get("/{id}")
def get_movie_detail(id: int):
    return {"_id": id}
