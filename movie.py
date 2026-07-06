import requests

api_key = "ENTER YOU KEY HERE"
movie = input("Enter your movie: ")

url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie}"

response = requests.get(url)
data = response.json()
movies = data['results']
first_movie = movies[0]

title = first_movie['title']
release_date = first_movie['release_date']
rating = first_movie['vote_average']
popularity = first_movie['popularity']
overview = first_movie['overview']

print(f"Movie: {title}")
print(f"Release date: {release_date}")
print(f"Rating: {round(rating, 1)}/10")
print(f"Popularity: {round(popularity, 1)}")
print(f"Overview: {overview}")