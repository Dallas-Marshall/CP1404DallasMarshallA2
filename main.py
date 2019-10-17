"""
Name: Dallas Marshall
Date: 17-10-2019
Brief Project Description: Graphical User Interface using kivy for assignment 2.
GitHub URL: https://github.com/cp1404-students/2019-2-a2-Dallas-Marshall
"""
# TODO: Create your main program in this file, using the MoviesToWatchApp class

from kivy.app import App
from moviecollection import MovieCollection
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ListProperty

sort_codes = ['year', 'title', 'category', 'is_watched']


class MoviesToWatchApp(App):
    """Kivy app constructor class to create GUI for assignment 2."""
    movies_to_watch_text = StringProperty()
    display_text = StringProperty()
    current_selection = StringProperty()
    sort_options = ListProperty()

    def __init__(self, **kwargs):
        """Load movies from movies.csv."""
        super().__init__(**kwargs)
        self.movies = MovieCollection()
        self.movies.load_movies('movies.csv')

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Movies To Watch 2.0"
        self.root = Builder.load_file('app.kv')
        self.sort_options = sorted(sort_codes)
        self.current_selection = self.sort_options[0]
        return self.root


if __name__ == '__main__':
    MoviesToWatchApp().run()
