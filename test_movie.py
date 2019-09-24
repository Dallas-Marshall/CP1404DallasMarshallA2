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


run_tests()
