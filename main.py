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
from kivy.uix.button import Button

sort_codes = ['year', 'title', 'category', 'is_watched']


class MoviesToWatchApp(App):
    """Kivy app constructor class to create GUI for assignment 2."""
    movies_to_watch_text = StringProperty()
    status_text = StringProperty()
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
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from MovieCollection entries and add them to the GUI."""
        for movie in self.movies.movies:
            # create a button for each data entry, specifying the text and id
            # (although text and id are the same in this case, you should see how this works)
            temp_button = Button(text=movie.title, id=movie.title)
            temp_button.bind(on_release=self.handle_press)
            temp_button.movie = movie
            # add the button to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_button)

    def handle_press(self, instance):
        """Handle pressing movie buttons."""
        movie = instance.movie
        # update status text
        unwatched_string = 'have watched'
        if not movie.is_watched:
            unwatched_string = 'need to watch'
        self.status_text = "You {} {}".format(unwatched_string, movie.title)


if __name__ == '__main__':
    MoviesToWatchApp().run()
