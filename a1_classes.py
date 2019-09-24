"""Copy of first assignment to reference"""
# TODO: Copy your first assignment to this file, then update it to use Movie class
# Optionally, you may also use MovieCollection class

from movie import Movie
import operator

INDEX_OF_TITLE = 0
INDEX_OF_YEAR = 1
INDEX_OF_CATEGORY = 2
INDEX_OF_STATUS = 3
FILE_NAME = 'movies.csv'
WATCHED = 'w'
UNWATCHED = 'u'


def main():
    """program is a list of movies that allows a user to track movies that they have watched and wish to watch."""
    movies = read_file()
    menu = """Menu:\nL - List movies\nA - Add new movie\nW - Watch a movie\nQ - Quit"""
    print("Movies To Watch 1.0 - by Dallas Marshall\n{} movies loaded\n{}".format(len(movies), menu))
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


def read_file():
    """Read the file containing movies saving as a list."""
    movies = []
    in_file = open('{}'.format(FILE_NAME), 'r')
    for line in in_file:
        line_str = line.strip().split(',')
        movie = [line_str[INDEX_OF_TITLE], int(line_str[INDEX_OF_YEAR]), line_str[INDEX_OF_CATEGORY],
                 line_str[INDEX_OF_STATUS]]
        movies.append(movie)
    in_file.close()
    return movies


def add_movie(movies):
    """Add new movie to list."""
    new_title = get_valid_selection("Title")
    new_year = get_valid_year()
    new_category = get_valid_selection("Category")
    movies.append([new_title, new_year, new_category, UNWATCHED])
    print("{} ({} from {}) added to movie list".format(new_title, new_category, new_year))


def list_movies(movies):
    """Sort movies by year and prints formatted table labeling unwatched with *."""
    movies.sort(key=operator.itemgetter(INDEX_OF_YEAR, INDEX_OF_TITLE))
    for i in range(len(movies)):
        unwatched_string = ' '
        if not is_watched(movies, i):
            unwatched_string = '*'
        print("{:2}. {} {:{}} - {:5} ({})".format(i, unwatched_string, movies[i][INDEX_OF_TITLE],
                                                  calculate_longest_title(movies), movies[i][INDEX_OF_YEAR],
                                                  movies[i][INDEX_OF_CATEGORY]))
    print("{} movies watched, {} movies still to watch".format(count_movies_status(movies, WATCHED),
                                                               count_movies_status(movies, UNWATCHED)))


def count_movies_status(movies, status):
    """Return count of status e.g. (watched (w) or unwatched(u)."""
    movie_count = 0
    for i in range(len(movies)):
        if movies[i][INDEX_OF_STATUS] == '{}'.format(status):
            movie_count += 1
    return movie_count


def is_watched(movies, i):
    """Return True if movie is watched, else returns False."""
    return bool(movies[i][INDEX_OF_STATUS].lower() == WATCHED)


def watch_movie(movies):
    """Set a chosen movie as watched."""
    if count_movies_status(movies, UNWATCHED) == 0:
        return print("No more movies to watch!")

    print("Enter the number of a movie to mark as watched")
    movie_index = get_valid_input(movies)

    if is_watched(movies, movie_index):
        print("You have already watched {}".format(movies[movie_index][INDEX_OF_TITLE]))
    else:
        movies[movie_index][INDEX_OF_STATUS] = WATCHED
        print("{} from {} watched".format(movies[movie_index][INDEX_OF_TITLE], movies[movie_index][INDEX_OF_YEAR]))


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


def calculate_longest_title(movies):
    """Return longest movie title length."""
    longest_title_length = 0
    for movie in movies:
        title_length = len(movie[INDEX_OF_TITLE])
        if title_length > longest_title_length:
            longest_title_length = title_length
    return longest_title_length


def get_valid_selection(prompt):
    """Return a valid (prompt).

     Keyword arguments:
     prompt -- the string displayed to the user
     """
    user_input = input("{}: ".format(prompt))
    while not user_input.strip():
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
    out_file = open('{}'.format(FILE_NAME), WATCHED)
    movies.sort(key=operator.itemgetter(1, 0))
    for movie in movies:
        line = convert_list_to_string(movie)
        out_file.write("{}\n".format(line))
    out_file.close()


def convert_list_to_string(movie):
    """Return a list as a string."""
    separator = ','
    for index, element in enumerate(movie):
        movie[index] = str(element)
    return separator.join(movie)


if __name__ == '__main__':
    main()
