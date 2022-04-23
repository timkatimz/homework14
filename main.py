from flask import Flask
from movie.views import movie
from rating.views import rating

app = Flask(__name__)
app.register_blueprint(movie)
app.register_blueprint(rating)

if __name__ == "__main__":
    app.run()
