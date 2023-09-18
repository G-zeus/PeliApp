import httpx

from ...config.config import get_settings


class TmDB:

    def __init__(self):
        self.base_url = get_settings().TMDB_API_URL

    def get_popular(self, page: int = 1) -> dict:
        uri = f"/movie/popular?language=en-US&page={page}"
        headers = {
            "accept": "application/json",
            "Authorization": get_settings().TMDB_AUTH_TOKEN
        }
        r = httpx.get(url=self.base_url + uri, headers=headers)

        return r.json()
