import sqlite3


def get_cast_list(actor_1, actor_2):
    with sqlite3.connect('netflix.db') as con:
        cur = con.cursor()
        data = cur.execute('SELECT "cast" '
                           'FROM netflix '
                           'WHERE "cast" LIKE "actor_1"=:actor_1 AND "cast" LIKE "actor_2"=:actor_2',
                           {"actor_1": actor_1,
                            "actor_2": actor_2}).fetchall()

        all_actors = []
        for actors in data:
            all_actors.extend(actors[0].split(", "))

        actors_list = []
        for actor in all_actors:
            if actor not in [actor_1, actor_2]:
                if all_actors.count(actor) > 2:
                    actors_list.append(actor)
        actors_list = set(actors_list)
        return list(actors_list)
        # print(list(actors_list))


get_cast_list("Rose McIver", "Ben Lamb")


def get_movies_by_type(type, genre, year):
    with sqlite3.connect('netflix.db') as con:
        cur = con.cursor()
        query = f"""
                SELECT title, description
                FROM netflix
                WHERE type = '{type}'
                AND listed_in LIKE '%{genre}%'
                AND release_year = {year}
                """

        cur.execute(query)
        data = cur.fetchall()

        movies_list = []
        for movies in data:
            movie = {
                "title": movies[0],
                "description": movies[1].strip()
            }
            movies_list.append(movie)
        print(movies_list)
        return movies_list

get_movies_by_type("Movie", "Dramas", 2010)
