from dotenv import load_dotenv

from api.TMDBApi import TMDBApi
from utils.support import user_input, print_table

# Load environment variables for api credentials
load_dotenv()

# User input for search query
query = user_input()

# Initialize TMDB api
tmdb_api = TMDBApi()

# Settings
page_counter = 1
total_pages_counter = 1

movies = []

# Paginate through movies pages
while page_counter <= total_pages_counter:
    # Get movies by search query
    retrieved_movies, total_pages = tmdb_api.get_movies(query, page_counter)

    for movie in retrieved_movies:
        movies.append(movie)

    page_counter += 1
    total_pages_counter = total_pages

# Print movie information as table
if movies:
    print(print_table(movies))
else:
    print('No movies found for search query "{}"'.format(query))
