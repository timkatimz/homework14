from flask import Blueprint, jsonify
from rating.utils import get_movie_by_rating

rating = Blueprint('rating', __name__, url_prefix="/rating")


@rating.route("/children")
def movie_for_children():
    children_rating = 'G', 'G'
    children_movies = get_movie_by_rating(children_rating)
    return jsonify(children_movies)


@rating.route("/family")
def movie_family():
    family_rating = 'G', 'PG', 'PG-13'
    family_movies = get_movie_by_rating(family_rating)
    return jsonify(family_movies)


@rating.route("/adult")
def movie_for_family():
    adult_rating = 'R', 'NC-17'
    adult_movies = get_movie_by_rating(adult_rating)
    return jsonify(adult_movies)
