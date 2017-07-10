import media
import fresh_tomatoes
import requests
from bs4 import BeautifulSoup
import re
import unicodedata

# Rotten Tomatoes request url
url = "https://www.rottentomatoes.com/browse/top-dvd-streaming?minTomato=70&maxTomato=100&minPopcorn=70&maxPopcorn=100&services=amazon;hbo_go;itunes;netflix_iw;vudu;amazon_prime;fandango_now&genres=1;2;4;5;6;8;9;10;11;13;18;14&sortBy=popularity" # NOQA

def scrape_movie_data(url):
    # Go to Rotten Tomatoes page that displays movie scores > 70%
    page = requests.get(url)

    # Get webpage's html output
    soup = BeautifulSoup(page.content, "html.parser")

    # Find script tag that generates our movie list
    script = soup.html.find('script', text=re.compile(r"\[{\"id\"\:"))

    # Scrape movie titles & scores
    pattern = re.compile(r"\{\"[a-z]*\".*\}")
    raw_data = re.findall(pattern, script.text)
    movie_data = raw_data[0]
    return movie_data

def normalize_data(raw_data):
    # Normalize scraped data
    movie_data_str = unicodedata.normalize('NFKD', raw_data).encode('ascii',
                                                                    'ignore')

    # movie_titles list
    pattern = re.compile(r"\"title\":\"([a-zA-Z0-9\s]*)")
    movie_titles = re.findall(pattern, movie_data_str)

    # tomato_scores list
    pattern = re.compile(r"\"tomatoScore\":([0-9]*)")
    tomato_scores = re.findall(pattern, movie_data_str)

    # popcorn_scores list
    pattern = re.compile(r"\"popcornScore\":([0-9]*)")
    popcorn_scores = re.findall(pattern, movie_data_str)

    # movie_storylines list
    pattern = re.compile(
        r"\"synopsis\":\"([<em>^A-Z0-9a-z\s/,'.()-;\\\"]*)(?=\"\,\"synopsisType)")
    movie_storylines = re.findall(pattern, movie_data_str)

    # poster_images list
    pattern = re.compile(r"\"primary\":\"([a-zA-Z0-9:\/._=-]*)")
    poster_images = re.findall(pattern, movie_data_str)

    # movie_trailers list
    pattern = re.compile(r"\"mainTrailer\":{\"sourceId\":\"([a-zA-Z0-9:\/._=-]*)")
    movie_trailers = re.findall(pattern, movie_data_str)

    # Create movie instances and assemble movies list
    movies = []  # The movie instances will go here
    length = len(movie_titles)  # Sets loop length
    index = 0
    while index < length:
        # Create movie instances for each movie and append to movies list
        movies.append(media.Movie(movie_titles[index],
                                  tomato_scores[index],
                                  popcorn_scores[index],
                                  movie_storylines[index],
                                  poster_images[index],
                                  movie_trailers[index]))
        index += 1
    return movies

def get_rt_movies(url):
    # Get movie data of all new release DVD movies with RT score > 70%/70%
    raw_movie_data = scrape_movie_data(url)

    # Normalize data
    movies = normalize_data(raw_movie_data)
    return movies

movies = get_rt_movies(url)  # Get movies list
fresh_tomatoes.open_movies_page(movies)  # Open movies website passing movies
