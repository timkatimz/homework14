import sqlite3


def get_movie_by_rating(rating):
    with sqlite3.connect('netflix.db') as con:
        cursor = con.cursor()
        query = f"""
            SELECT title, rating, description
            FROM 'netflix'
            WHERE rating IN {rating} 
            AND rating != ''
            AND rating IS NOT NULL
            LIMIT 100
        """

        res = cursor.execute(query)
        data = res.fetchall()

        movies_list = []
        for movies in data:
            movie = {
                "title": movies[0],
                "rating": movies[1],
                "description": movies[2]
            }
            movies_list.append(movie)

        return movies_list
