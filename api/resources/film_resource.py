from flask_restful import Resource, reqparse
from logic.film_logic import FilmLogic


class Film(Resource):
    def __init__(self):
        self.film_put_args = self.createParser()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("title", type=str, help=" ")
        args.add_argument("description", type=str, help=" ")
        args.add_argument("release_year", type=int, help="")
        args.add_argument("language_id", type=int, help="")
        args.add_argument("original_language_id", type=int, help="")
        args.add_argument("rental_duration", type=int, help="")
        args.add_argument("rental_rate", type=float, help="")
        args.add_argument("length", type=str, help="")
        args.add_argument("replacement_cost", type=float, help="")
        args.add_argument("rating", type=float, help="")
        args.add_argument("special_features", type=str, help="")
        args.add_argument("last_update", type=float, help="")
        return args

    def get(self, id):
        logic = FilmLogic()
        result = logic.getFilmById(id)
        if len(result) == 0:
            return {}
        return result[0], 200

    def post(self, id):
        logic = FilmLogic()
        result = logic.postFilmById(id)
        if len(result) == 0:
            return {}
        return result[0], 200

    def put(self, id):
        film = self.film_put_args.parse_args()
        logic = FilmLogic()
        rows = logic.insertFilm(film)
        return {"rowsAffected": rows}, 200

    def patch(self, id):
        film = self.film_put_args.parse_args()
        logic = FilmLogic()
        rows = logic.updateFilm(id, film)
        return {"rowsAffected": rows}, 200

    def delete(self, id):
        logic = FilmLogic()
        rows = logic.deleteFilm(id)
        return {"rowsAffected": rows}, 200
