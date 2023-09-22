from ..TmDB import TmDB
from ..contracts.MovieData import MovieData


class MovieTmDBDataAdapter(MovieData, TmDB):

    def get_popular(self, page: int = 1) -> dict:
        data = self.get_TmDB_popular(page=page)
        filtered = self.format_movies_response(data['results'])
        return {
            "page": data['page'],
            "movies": filtered
        }

    def get_search(self, search: str) -> dict:
        data = self.search_movie(search=search)
        filtered = self.format_movies_response(data['results'])
        return {
            "page": data['page'],
            "movies": filtered
        }

    def get_movie_by_id(self, id: int) -> dict:
        data = self.get_TmDB_movie(id=id)

        return {
            "movie":
                {
                    "id": data["id"],
                    "title": data["title"],
                    "releaseYear": data["release_date"][0:4],
                    "releaseDate": data["release_date"],
                    "posterImage": self.base_img_url + data["poster_path"] if data["poster_path"] is not None
                    else self.img_default,
                    "backdropImage": self.base_img_url + data["backdrop_path"] if data["backdrop_path"] is not None
                    else self.img_default,
                    "overview": data["overview"],
                    "runtime": data["runtime"],
                    "genres": [v['name'] for v in data["genres"]],
                    "averageRating": data["vote_average"]
                }
        }

    def format_movies_response(self, data: list) -> list:
        filtered = []
        for v in data:
            filtered.append(
                {
                    "id": v["id"],
                    "title": v["title"],
                    "releaseYear": v["release_date"][0:4],
                    "posterImage": self.base_img_url + v["poster_path"] if v["poster_path"] is not None
                    else self.img_default,
                    "overview": v["overview"][0:100] + "..."
                }
            )
        return filtered
