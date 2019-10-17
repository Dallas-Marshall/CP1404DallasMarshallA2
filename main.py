"""
Name: Dallas Marshall
Date: 17-10-2019
Brief Project Description: Graphical User Interface using kivy for assignment 2.
GitHub URL: https://github.com/cp1404-students/2019-2-a2-Dallas-Marshall
"""
# TODO: Create your main program in this file, using the MoviesToWatchApp class

from kivy.app import App
from moviecollection import MovieCollection


class MoviesToWatchApp(App):
    """Kivy app constructor class to create GUI for assignment 2."""

    def __init__(self, **kwargs):
        """Load movies from movies.csv."""
        super().__init__(**kwargs)
        self.movies = MovieCollection()
        self.movies.load_movies('movies.csv')


if __name__ == '__main__':
    MoviesToWatchApp().run()
