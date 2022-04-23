from flask import Blueprint, jsonify
from movie.utils import get_movie_by_name, get_movie_by_years

movie = Blueprint('movie', __name__, url_prefix='/movie')


@movie.route("/<title>")
def show_movie_by_name(title):
    movies = get_movie_by_name(title)
    return jsonify(movies)


@movie.route("/<from_year>/to/<to_year>")
def movies_by_years(from_year, to_year):
    movies = get_movie_by_years(from_year, to_year)
    return jsonify(movies)
