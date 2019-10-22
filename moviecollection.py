"""Movie collection class for assignment 2."""
from movie import Movie
from operator import attrgetter

INDEX_OF_TITLE = 0
INDEX_OF_YEAR = 1
INDEX_OF_CATEGORY = 2
INDEX_OF_STATUS = 3
WATCHED = 'w'
UNWATCHED = 'u'

class MovieCollection:
    """A class to keep track of a list of Movie objects."""

    def __init__(self):
        """Initialise empty list to store movie objects."""
        self.movies = []

    def __str__(self):
        """Return a string representation of movie_collection."""
        return str([str(movie) for movie in self.movies])

    def __len__(self):
        return len(self.movies)

    def add_movie(self, movie):
        """Add a movie to the list of movies."""
        self.movies.append(movie)

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
        # index_of_title = 0
        # index_of_year = 1
        # index_of_category = 2
        # index_of_status = 3

        in_file = open('{}'.format(file_name), 'r')
        for line in in_file:
            line_str = line.strip().split(',')
            # Create movie instance and convert year to an integer
            movie = Movie(line_str[INDEX_OF_TITLE], int(line_str[INDEX_OF_YEAR]), line_str[INDEX_OF_CATEGORY],
                          True if line_str[INDEX_OF_STATUS] == WATCHED else False)
            self.movies.append(movie)
        in_file.close()

    def save_movies(self, filename):
        """Save movies to file."""
        out_file = open('{}'.format(filename), 'w')
        for movie in self.movies:
            out_file.write("{}\n".format(movie))
        out_file.close()

    def sort_movies(self, keyword):
        """Sort objects by keyword attribute."""
        self.movies.sort(key=attrgetter(keyword, "title"))

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

    def set_movie_watched(self, movie_index):
        """Set movie at specified index watched if not already."""
        if self.movies[movie_index].is_watched:
            print("You have already watched {}".format(self.movies[movie_index].title))
        else:
            self.movies[movie_index].watch_movie()
            print("{} from {} watched".format(self.movies[movie_index].title, self.movies[movie_index].year))

    def bool_to_status(self):
        """Set is_watched to 'w' or 'u' ready for saving so that it matched sample output."""
        for movie in self.movies:
            if movie.is_watched:
                movie.is_watched = WATCHED
            else:
                movie.is_watched = UNWATCHED
