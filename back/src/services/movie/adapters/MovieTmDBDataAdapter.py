from ..TmDB import TmDB
from ..contracts.MovieData import MovieData


class MovieTmDBDataAdapter(MovieData, TmDB):

    def get_popular(self, page: int = 1) -> dict:
        print(page)
        data = self.get_TmDB_popular(page=page)
        filtered = []
        for v in data['results']:
            filtered.append(
                {
                    "id": v["id"],
                    "title": v["title"],
                    "releaseYear": v["release_date"][0:4],
                    "posterImage": self.base_img_url + v["poster_path"],
                    "overview": v["overview"]
                }
            )
        return {
            "page": data['page'],
            "movies": filtered
        }
