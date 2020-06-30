from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False)
    actors = db.Column(db.String(50), unique=False)

    def __init__(self, title, actors):
        self.title = title
        self.actors = actors

class MoviesSchema(ma.Schema):
    class Meta:
        fields = ('title', 'actors')
movie_schema = MoviesSchema()
movies_schema = MoviesSchema(many=True)

@app.route("/")
def home():
     return "Hello There!"

@app.route('/movie', methods=["POST"])
def add_movies():
    title = request.json['title']
    actors = request.json['actors']
    new_movies = Movies(title, actors)
    db.session.add(new_movies)
    db.session.commit()

    movies = Movies.query.get(new_movies.id)

    return movies_schema.jsonify(movies)

@app.route("/movies", methods=["GET"])
def get_movie():
    all_movies = Movies.query.all()
    result = movies_schema.dump(all_movies)
    return jsonify(result)

@app.route("/movies/<id>", methods=["GET"])
def get_movies(id):
    movies = Movies.query.get(id)
    return movies_schema.jsonify(movies)

@app.route("/movies/<id>", methods=["PUT"])
def movies_update(id):
    movies = Movies.query.get(id)
    title = request.json['title']
    actors = request.json['actors']

    movies.title = title
    movies.actors = actors

    db.session.commit()
    return movies_schema.jsonify(movies)

@app.route("/movies/<id>", methods=["DELETE"])
def movies_delete(id):
    movies = Movies.query.get(id)
    db.session.delete(movies)
    db.session.commit()

    return "Movies were successfully deleted"





if __name__ == '__main__':
    app.run(debug=True)