from ..services.movie.TmDB import TmDB


class Movie:

    def __init__(self):
        self.movie_data = TmDB()

    def get_popular(self, page: int = 0):
        return {"data": {"page": page, "movies": self.movie_data.get_popular(page=page)}}
