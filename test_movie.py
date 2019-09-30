"""(Incomplete) Tests for Movie class."""
from movie import Movie


def run_tests():
    """Test Movie class."""

    # Test empty movie (defaults)
    print("Test empty movie:")
    default_movie = Movie()
    print(default_movie)
    assert default_movie.title == ""
    assert default_movie.category == ""
    assert default_movie.year == 0
    assert not default_movie.is_watched

    # Test initial-value movie
    initial_movie = Movie("Thor: Ragnarok", 2017, "Comedy", True)

    # TODO: Write tests to show this initialisation works
    print("Test Initial Movie:")
    print("Output:\n\tExpected: Thor: Ragnarok,2017,Comedy,True \n\tgot;      {}".format(initial_movie))
    print("Title:\n\tExpected: Thor: Ragnarok - <class 'str'>\n\tgot;      {} - {}".format(initial_movie.title,
                                                                                           type(initial_movie.title)))
    print("Year:\n\tExpected: 2017 - <class 'int'>\n\tgot;      {} - {}".format(initial_movie.year,
                                                                                type(initial_movie.year)))
    print("Category:\n\tExpected: Comedy - <class 'str'>\n\tgot;      {} - {}".format(initial_movie.category,
                                                                                      type(initial_movie.category)))
    # TODO: Add more tests, as appropriate, for each method
    # test watch_movie changes is_watched
    test_movie_1 = Movie("Super-man", 2008, "Comedy", False)
    print("\nTest watch_movie method:")
    print("\tBefore - Expected False got {}".format(test_movie_1.is_watched))
    test_movie_1.watch_movie()
    print("\tAfter - Expected True got {}".format(test_movie_1.is_watched))

    # Test condition of already watched movie
    test_movie_2 = Movie("Super-man", 2008, "Comedy", True)
    print("\nTest condition of already watched movie:\n\tExpected: You have already watched {}\n\tGot;"
          .format(test_movie_2.title))
    test_movie_2.watch_movie()

    # test condition when all movies are watched
    Movie.IS_ALL_MOVIES_WATCHED = True
    test_movie_3 = Movie("Super-man", 2008, "Comedy", False)
    print("\nTest condition when all movies are watched:\n\tExpected: No more movies to watch!\n\tGot;")
    test_movie_3.watch_movie()

    # test un_watch_movie changes is_watched
    test_movie_4 = Movie("Super-man", 2008, "Comedy", True)
    print("\nTest un_watch_movie method:")
    print("\tBefore - Expected True got {}".format(test_movie_4.is_watched))
    test_movie_4.un_watch_movie()
    print("\tAfter - Expected False got {}".format(test_movie_4.is_watched))


run_tests()
