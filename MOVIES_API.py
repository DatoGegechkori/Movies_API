import requests
import json
import sqlite3

key = '1064d8e6'
movie_name = input("Enter a movie name: ")

url = f'http://www.omdbapi.com/?apikey={key}&t={movie_name}'
response = requests.get(url)

print(f'Status code: {response.status_code}')
print(f'Headers: {response.headers}')
print(f'Text: {response.text}')

content = response.json()
print(json.dumps(content, indent=4))

print(f"Title: {content['Title']}")
print(f"Year: {content['Year']}")
print(f"Director: {content['Director']}")
print(f"Actors: {content['Actors']}")
print(f"Plot: {content['Plot']}")
print(f"Rating: {content['imdbRating']}")

# SQlite table showing movie title, year, director, actors, number of votes and imdb rating
conn = sqlite3.connect('movies.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        title,
        year,
        director,
        actors,
        votes,
        rating)
''')
c.execute('INSERT INTO movies (title, year, director, actors, votes, rating) VALUES (?,?,?,?,?,?)', (content['Title'], content['Year'], content['Director'], content['Actors'], content['imdbVotes'], content['imdbRating']))
conn.commit()
conn.close()
