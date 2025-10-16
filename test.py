""" File One
Simply Print the titles of all movies

File Two
After accepting user input, print all movies that released AFTER a given year.

File Three
After accepting user input, print all movies that released AFTER a given year and BEFORE a different year.

File 4
After accepting user input, print all movies that released during a given year.

File 5
Develop a function that allows users to search for a specific movie and returns all results that match

File 6
Develop a function that allows users to search for movies by genre """


import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)


#File One

""" for i in range(len(data)):
    print(data[i]['title']) """

#File Two

""" def releaseyear(year_release):
    year_release = input("WRITE A YEAR TO FIND A MOVIE.")
    year_release = int(year_release)
    for i in range(len(data)):
        if (data[i]['year']) > year_release:
            print(data[i]['title'])
releaseyear(2021) """

#File Three

""" def releaserange(year_release, cutoff_year):
    year_release = int(year_release)
    cutoff_year = int(cutoff_year)
    print(f"THE MOVIES THAT RELEASED BETWEEN {year_release} AND {cutoff_year} ARE:")
    for i in range(len(data)):
        if data[i]['year'] > year_release and data[i]['year'] < cutoff_year:
            print(data[i]['title'])
releaserange(2020, 2023) """

#File Four

""" def exactreleaseyear(year_release):
    year_release = int(year_release)
    print(f"THE MOVIES THAT RELEASED DURING {year_release} ARE:")
    for i in range(len(data)):
        if data[i]['year'] == year_release:
            print(data[i]['title'])
exactreleaseyear(2023) """

#File Five

""" def moviesearch(movie_name):
    movie_results = 0
    print(f"HERE ARE THE RESULTS FOR {movie_name}:")
    for i in range(len(data)):
        if (data[i]['title']) == movie_name:
            print(data[i])
            movie_results = movie_results + 1
    if movie_results == 0:
        print("THERE ARE NO MOVIES WITH THAT NAME. SEARCH AGAIN.")
moviesearch("M3GAN") """

#File Six

def genresearch(genre_names):
    genre_names = genre_names.split(", ")
    movie_results = 0
    print(f"HERE ARE THE RESULTS FOR {genre_names}:")
    for i in range(len(data)):
        if (data[i]['genres']) in genre_names:
            print(data[i]['title'])
            movie_results = movie_results + 1
    if movie_results == 0:
        print("THERE ARE NO MOVIES WITH THAT GENRE/GENRES. SEARCH AGAIN.")
genresearch("Horror")