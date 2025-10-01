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

""" year_release = input("WRITE A YEAR TO FIND A MOVIE.")
year_release = int(year_release)
for i in range(len(data)):
    if (data[i]['year']) > year_release:
        print(data[i]['title']) """

#File Three

""" year_release = input("WRITE A YEAR TO FIND A MOVIE.")
cutoff_year = input("WRITE ANOTHER YEAR THAT IS LARGER THAN THE FIRST.")
year_release = int(year_release)
cutoff_year = int(cutoff_year)
print(f"THE MOVIES THAT RELEASED BETWEEN {year_release} AND {cutoff_year} ARE:")
for i in range(len(data)):
    if data[i]['year'] > year_release and data[i]['year'] < cutoff_year:
        print(data[i]['title']) """

#File Four