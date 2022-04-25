import sqlite3


def get_movie_by_genre(genre):
    with sqlite3.connect('netflix.db') as con:
        cur = con.cursor()
        query = f"""
        SELECT title, description
        FROM netflix
        WHERE listed_in LIKE '%{genre}%'
        LIMIT 100
        """

        cur.execute(query)
        data = cur.fetchall()
        movies_list = []
        for movie in data:
            movies = {
                "title": movie[0],
                "description": movie[1].strip()
            }
            movies_list.append(movies)
        return movies_list
