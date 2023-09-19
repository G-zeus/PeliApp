import httpx

from ...config.config import get_settings


class TmDB:

    def __init__(self):
        self.base_url = get_settings().TMDB_API_URL
        self.base_img_url = get_settings().TMDB_IMG_URL
        self.headers = {
            "accept": "application/json",
            "Authorization": get_settings().TMDB_AUTH_TOKEN
        }

    def get_TmDB_popular(self, page: int = 1) -> dict:
        uri = f"/movie/popular?language=en-US&page={page}"
        r = httpx.get(url=self.base_url + uri, headers=self.headers)
        return r.json()

    def search_movie(self, search: str) -> dict:
        uri = f"/search/movie?query={search}&include_adult=false&language=en-US&page=1"
        r = httpx.get(url=self.base_url + uri, headers=self.headers)
        return r.json()

    def get_TmDB_movie(self, id: int) -> dict:
        uri = f"/movie/{id}?language=en-US"
        r = httpx.get(url=self.base_url + uri, headers=self.headers)
        return r.json()
