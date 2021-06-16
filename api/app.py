from flask import Flask
from flask_restful import Api
from resources.film_resource import Film

app = Flask(__name__)
api = Api(app)

api.add_resource(Film, "/film/<int:id>")

if __name__ == "__main__":
    app.run(debug=True, port=23512)