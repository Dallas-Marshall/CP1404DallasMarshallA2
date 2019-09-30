"""Movie collection class for assignment 2."""
from movie import Movie


class MovieCollection:
    """A class to keep track of a list of Movie objects."""

    def __init__(self):
        """Initialise empty list to store movie objects."""
        self.movies = []

    def __str__(self):
        """Return a string representation of movie_collection."""
        return str([str(movie) for movie in self.movies])
