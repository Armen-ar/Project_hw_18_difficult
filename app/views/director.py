from flask_restx import Namespace, Resource

from app.dao.model.director import DirectorsSchema
from app.implemented import director_service

director_ns = Namespace('directors')

director_schema = DirectorsSchema()
directors_schema = DirectorsSchema(many=True)


@director_ns.route('/')
class MoviesView(Resource):
    def get(self):
        all_directors = director_service.get_all()

        return directors_schema.dump(all_directors), 200


@director_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid: int):
        director = director_service.get_one(uid)

        return director_schema.dump(director), 200
