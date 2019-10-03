"""Movie collection class for assignment 2."""
from movie import Movie
from operator import attrgetter


class MovieCollection:
    """A class to keep track of a list of Movie objects."""

    def __init__(self):
        """Initialise empty list to store movie objects."""
        self.movies = []

    def __str__(self):
        """Return a string representation of movie_collection."""
        return str([str(movie) for movie in self.movies])

    def add_movie(self, movie):
        """Add a movie to the list of movies."""
        self.movies.append(movie)
        print("{self.title} ({self.category} from {self.year}) added to movie list".format(self=movie))

    def get_number_un_watched(self):
        """Returns number of movies unwatched."""
        movies_un_watched = 0
        for movie in self.movies:
            if not movie.is_watched:
                movies_un_watched += 1
        return movies_un_watched

    def get_number_watched(self):
        """Returns number of movies watched."""
        movies_watched = 0
        for movie in self.movies:
            if movie.is_watched:
                movies_watched += 1
        return movies_watched

    def load_movies(self, file_name):
        """Read the file containing movies saving as a list."""
        index_of_title = 0
        index_of_year = 1
        index_of_category = 2
        index_of_status = 3

        in_file = open('{}'.format(file_name), 'r')
        for line in in_file:
            line_str = line.strip().split(',')
            movie = Movie(line_str[index_of_title], int(line_str[index_of_year]), line_str[index_of_category],
                          True if line_str[index_of_status] == 'w' else False)
            self.movies.append(movie)
        in_file.close()

    def save_movies(self, filename):
        """Save movies to file."""
        out_file = open('{}'.format(filename), 'w')
        for movie in self.movies:
            out_file.write("{}\n".format(movie))
        out_file.close()

    def sort(self, keyword):
        """Sort objects by keyword attribute."""
        self.movies.sort(key=attrgetter(keyword, "title"))

    def __len__(self):
        return len(self.movies)

    def calculate_longest_title(self):
        """Return longest movie title length."""
        longest_title_length = 0
        for movie in self.movies:
            title_length = len(movie.title)
            if title_length > longest_title_length:
                longest_title_length = title_length
        return longest_title_length

    def list_movies(self, longest_title_length):
        """Sort movies by year and prints formatted table labeling unwatched with *."""
        for i, movie in enumerate(self.movies):
            unwatched_string = ' '
            if not movie.is_watched:
                unwatched_string = '*'
            print("{:2}. {} {:{}} - {:5} ({})".format(i, unwatched_string, movie.title, longest_title_length,
                                                      movie.year, movie.category))
