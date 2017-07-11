import webbrowser


class Movie():
    """Movie object that contains:

    Attributes:
        movie_title (str): Title of movie.
        tomato_score (str): Percentage of critics positive reviews.
        popcorn_score (str): Percentage of audience positive reviews.
        movie_storyline (str): Synopsis of movie plot.
        poster_image (str): Url of movie's poster image.
        movie_trailer (str): Url of movie's trailer
    """
    def __init__(self, movie_title, tomato_score, popcorn_score,
                 movie_storyline, poster_image, movie_trailer):
        self.title = movie_title
        self.tomato_score = tomato_score
        self.popcorn_score = popcorn_score
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_url = movie_trailer
