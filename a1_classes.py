"""Movie program from assignment 1, re-written using Movie and MovieCollection classes."""

from movie import Movie
from moviecollection import MovieCollection

FILE_NAME = 'movies.csv'
SORT_CONDITION = 'year'


def main():
    """Program is a list of movies that allows a user to track movies that they have watched and wish to watch."""
    movies = MovieCollection()
    movies.load_movies(FILE_NAME)
    movies.sort_movies(SORT_CONDITION)
    menu = """Menu:\nL - List movies\nA - Add new movie\nW - Watch a movie\nQ - Quit"""
    print("Movies To Watch 2.0 - by Dallas Marshall\n{} movies loaded\n{}".format(len(movies), menu))
    menu_selection = input(">>> ").upper()
    while menu_selection != 'Q':
        if menu_selection == 'L':
            list_movies(movies)
        elif menu_selection == 'A':
            add_movie(movies)
        elif menu_selection == 'W':
            watch_movie(movies)
        else:
            print("Invalid menu choice")
        print(menu)
        menu_selection = input(">>> ").upper()
    print("{} movies saved to {}\nHave a nice day :)".format(len(movies), FILE_NAME))
    save_movies(movies)


def list_movies(movies):
    longest_title_length = movies.calculate_longest_title()
    movies.sort_movies(SORT_CONDITION)

    movies.list_movies(longest_title_length)
    print("{} movies watched, {} movies still to watch".format(movies.get_number_watched(),
                                                               movies.get_number_un_watched()))


def add_movie(movies):
    """Add new movie to list."""
    new_title = get_valid_selection("Title")
    new_year = get_valid_year()
    new_category = get_valid_selection("Category")
    movies.add_movie(Movie(new_title, new_year, new_category, False))
    print("{} ({} from {}) added to movie list".format(new_title, new_category, new_year))
    movies.sort_movies(SORT_CONDITION)


def watch_movie(movies):
    """Set a chosen movie as watched."""
    if movies.get_number_un_watched() == 0:
        return print("No more movies to watch!")
    print("Enter the number of a movie to mark as watched")
    movie_index = get_valid_input(movies)
    movies.set_movie_watched(movie_index)


def get_valid_input(movies):
    """Return valid movie index input. """
    is_valid_input = False
    while not is_valid_input:
        try:
            movie_index = int(input(">>> "))
            if movie_index < 0:
                print("Number must be >= 0")
            elif movie_index > (len(movies) - 1):
                print("Invalid movie number")
            else:
                is_valid_input = True
                return movie_index
        except ValueError:
            print("Invalid input; enter a valid number")


def get_valid_selection(prompt):
    """Return a valid (prompt).

     Keyword arguments:
     prompt -- the string displayed to the user
     """
    user_input = input("{}: ".format(prompt))
    while user_input == "":
        print("Input can not be blank")
        user_input = input("{}: ".format(prompt))
    return user_input


def get_valid_year():
    """Return a valid year input."""
    is_valid_year = False
    while not is_valid_year:
        try:
            new_year = int(input("Year: "))
            if new_year < 0:
                print("Number must be >= 0")
            else:
                is_valid_year = True
                return new_year
        except ValueError:
            print("Invalid input; enter a valid number")


def save_movies(movies):
    """Save movies to file."""
    movies.bool_to_status()
    movies.save_movies(FILE_NAME)


if __name__ == '__main__':
    main()
