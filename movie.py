"""Movie class for assignment 2."""


# TODO: Create your Movie class in this file


class Movie:
    """Movie class to represent details of a movie."""

    def __init__(self, title="", year=0, category="", is_watched=False):
        """Initialise a Movie."""
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched

    def __str__(self):
        """Return a string representation of Guitar."""
        return "{self.title},{self.year},{self.category},{self.is_watched}".format(self=self)

    def watch_movie(self):
        """Set a Movie as watched."""
        if not self.is_watched:
            self.is_watched = True
            return print("{self.title} from {self.year} watched".format(self=self))
        else:
            return print("You have already watched {self.title}".format(self=self))

    def un_watch_movie(self):
        """Set a movie as un-watched."""
        if self.is_watched:
            self.is_watched = False
            return print("{self.title} from {self.year} un-watched".format(self=self))
