from flask import Flask
from movie.views import movie
from rating.views import rating
from genre.views import genre

app = Flask(__name__)
app.register_blueprint(movie)
app.register_blueprint(rating)
app.register_blueprint(genre)


if __name__ == "__main__":
    app.run()
