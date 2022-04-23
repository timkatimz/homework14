import sqlite3



def get_movie_by_name(title):
    with sqlite3.connect('netflix.db') as con:
        cur = con.cursor()
        query = f"""
        SELECT title, country, release_year, listed_in, description
        FROM netflix
        WHERE title = '{title}'
        ORDER BY date_added DESC 
        LIMIT 2
        """
        data = cur.execute(query)
        res = data.fetchall()

        movie = [{
            "title": res[0][0],
            "country": res[0][1],
            "release_year": res[0][2],
            "genre": res[0][3],
            "description": res[0][4]
        }]
        return movie


def get_movie_by_years(from_, to):
    with sqlite3.connect('netflix.db') as con:
        cur = con.cursor()
        query = f"""
        SELECT title, release_year
        FROM netflix
        WHERE release_year BETWEEN {from_} AND {to}
        ORDER BY release_year DESC 
        LIMIT 100
        """
        data = cur.execute(query)
        res = data.fetchall()
        movies_list = []

        for movies in res:
            movie = {
                "title": movies[0],
                "release_year": movies[1],
            }
            movies_list.append(movie)
        return movies_list

