from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):

        return self.dao.get_one(mid)

    def get_all(self):

        return self.dao.get_all()

    def create(self, data):

        return self.dao.create(data)

    def update(self, data):
        mid = data.get("id")
        movie = self.get_one(mid)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        self.dao.update(data)

    def update_partial(self, data):
        mid = data.get("id")
        author = self.get_one(mid)

        if "title" in data:
            author.title = data.get("title")
        if "description" in data:
            author.description = data.get("description")
        if "trailer" in data:
            author.trailer = data.get("trailer")
        if "year" in data:
            author.year = data.get("year")
        if "rating" in data:
            author.rating = data.get("rating")
        if "genre_id" in data:
            author.genre_id = data.get("genre_id")
        if "director_id" in data:
            author.director_id = data.get("director_id")

        self.dao.update(data)

    def delete(self, mid):
        self.dao.delete(mid)
