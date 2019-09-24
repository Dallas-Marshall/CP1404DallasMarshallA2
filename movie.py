"""Movie class for assignment 2."""


# TODO: Create your Movie class in this file


class Movie:
    """Movie class to represent details of a movie."""
    IS_ALL_MOVIES_WATCHED = False

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
        if not Movie.IS_ALL_MOVIES_WATCHED:
            if not self.is_watched:
                self.is_watched = True
                return print("{self.title} from {self.year} watched".format(self=self))
            else:
                return print("You have already watched {self.title}".format(self=self))
        else:
            return print("No more movies to watch!")
