from flask import Blueprint, jsonify
from genre.utils import get_movie_by_genre

genre = Blueprint('genre', __name__,)


@genre.route("/genre/<genre>")
def movies_by_genre(genre):
    data = get_movie_by_genre(genre)
    return jsonify(data)
