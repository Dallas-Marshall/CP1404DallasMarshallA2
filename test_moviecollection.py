"""(Incomplete) Tests for MovieCollection class."""
from movie import Movie
from moviecollection import MovieCollection


def run_tests():
    """Test MovieCollection class."""

    # Test empty MovieCollection (defaults)
    print("Test empty MovieCollection:")
    movie_collection = MovieCollection()
    print(movie_collection)
    assert not movie_collection.movies  # an empty list is considered False

    # Test loading movies
    print("\nTest loading movies:")
    movie_collection.load_movies('movies.csv')
    print(movie_collection)
    assert movie_collection.movies  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Movie with values
    print("\nTest adding new movie:")
    movie_collection.add_movie(Movie("Amazing Grace", 2006, "Drama", False))
    print(movie_collection)

    # Test sorting movies
    print("\nTest sorting - year:")
    movie_collection.sort_movies("year")
    print(movie_collection)

    print("\nTest sorting - title:")
    movie_collection.sort_movies("title")
    print(movie_collection)

    # Test saving movies (check CSV file manually to see results)
    movie_collection.save_movies('test.csv')

    # test number of un/watched movies
    print("\nTest get_number_watched:")
    print("expected 2 got {}".format(movie_collection.get_number_watched()))

    print("\nTest get_number_un_watched")
    print("expected 4 got {}".format(movie_collection.get_number_un_watched()))

    # Test length of movies
    print("\nTest __len__:")
    print("Expected 6 got {}".format(len(movie_collection)))

    print("\nTest calculate_longest_title:")
    print("Expected 34 got {}".format(movie_collection.calculate_longest_title()))

    print("\nTest list_movies prints to console:")
    longest_title_length = 35
    movie_collection.sort_movies('year')
    movie_collection.list_movies(longest_title_length)

    print("\nTest set_movie_watched:")
    movie_collection.set_movie_watched(0)
    movie_collection.list_movies(35)
    movie_collection.set_movie_watched(0)

    print("\nTest bool_to_status:")
    print(movie_collection)
    movie_collection.bool_to_status()
    print(movie_collection)


run_tests()
