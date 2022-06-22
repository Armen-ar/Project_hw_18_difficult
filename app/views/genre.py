from flask_restx import Namespace, Resource

from app.dao.model.genre import GenresSchema
from app.implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenresSchema()
genres_schema = GenresSchema(many=True)


@genre_ns.route('/')
class MoviesView(Resource):
    def get(self):
        all_genres = genre_service.get_all()

        return genres_schema.dump(all_genres), 200


@genre_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid: int):
        genre = genre_service.get_one(uid)

        return genre_schema.dump(genre), 200
