"""Movie class for assignment 2."""


# TODO: Create your Movie class in this file


class Movie:
    """Movie class to represent details of a Movie."""

    def __init__(self, title="", year=0, category="", is_watched=False):
        """Initialise a Movie."""
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched

    def __str__(self):
        """Return a string representation of Movie."""
        return "{self.title},{self.year},{self.category},{self.is_watched}".format(self=self)

    def watch_movie(self):
        """Set a Movie as watched."""
        self.is_watched = True

    def un_watch_movie(self):
        """Set a Movie as un-watched."""
        self.is_watched = False
