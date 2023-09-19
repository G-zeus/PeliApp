class MovieData:

    def get_popular(self) -> dict:
        return {"movies": {"id": "", "title": "", "releaseYear": "", "posterImage": "", "overview": ""}}

    def get_search(self, search: str) -> dict:
        return {"movies": {"id": "", "title": "", "releaseYear": "", "posterImage": "", "overview": ""}}

    def get_movie_by_id(self, id: int) -> dict:
        return {
            "movie":
                {
                    "id": "",
                    "title": "",
                    "releaseYear": "",
                    "releaseDate": "",
                    "posterImage": "",
                    "backdropImage": "",
                    "overview": "",
                    "runtime": "",
                    "genres": "",
                    "averageRating": "",
                }
        }
