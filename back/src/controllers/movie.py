from ..services.movie.adapters.MovieTmDBDataAdapter import MovieTmDBDataAdapter


class Movie:

    def __init__(self):
        self.movie_data = MovieTmDBDataAdapter()

    def get_popular(self, page: int = None):
        return self.movie_data.get_popular(page=page)

    def get_movie(self, id: int):
        return self.movie_data.get_movie_by_id(id=id)

    def search(self, search: str):
        return self.movie_data.get_search(search=search)
