from ..services.movie.adapters.MovieTmDBDataAdapter import MovieTmDBDataAdapter


class Movie:

    def __init__(self):
        self.movie_data = MovieTmDBDataAdapter()

    def get_popular(self, page: int = None):
        return self.movie_data.get_popular(page=page)
