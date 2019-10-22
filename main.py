"""
Name: Dallas Marshall
Date: 17-10-2019
Brief Project Description: Graphical User Interface using kivy for assignment 2.
GitHub URL: https://github.com/cp1404-students/2019-2-a2-Dallas-Marshall
"""
from kivy.app import App
from moviecollection import MovieCollection
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.uix.button import Button
from movie import Movie

SPINNER_OPTIONS_TO_KEYWORD = {'Year': 'year', 'Title': 'title', 'Category': 'category', 'Watched': 'is_watched'}
WATCHED_COLOR = (1, 0, 0, 1)
UN_WATCHED_COLOR = (1, 0, 1, 1)
FILE_NAME = 'movies.csv'


class MoviesToWatchApp(App):
    """Kivy app constructor class to create GUI for assignment 2."""
    movies_to_watch_text = StringProperty()
    status_text = StringProperty()
    current_selection = StringProperty()
    sort_options = ListProperty()

    def __init__(self, **kwargs):
        """Load movies from file."""
        super().__init__(**kwargs)
        self.movie_collection = MovieCollection()
        self.movie_collection.load_movies(FILE_NAME)

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Movies To Watch 2.0"
        self.root = Builder.load_file('app.kv')
        self.sort_options = sorted(SPINNER_OPTIONS_TO_KEYWORD.keys())
        self.current_selection = self.sort_options[0]
        self.movies_to_watch_text = "To watch: {} Watched: {}".format(self.movie_collection.get_number_un_watched(),
                                                                      self.movie_collection.get_number_watched())
        return self.root

    def create_widgets(self):
        """Create buttons from MovieCollection entries and add them to the GUI."""
        for movie in self.movie_collection.movies:
            display_color = self.set_button_color(movie)
            # create a button for each data entry, specifying the text and id
            temp_button = Button(
                text=self.display_watched(movie), id=movie.title, background_color=display_color)
            temp_button.bind(on_release=self.handle_press_movie)
            # Store a reference to the movie object in the button object
            temp_button.movie = movie
            # add the button to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_button)

    @staticmethod
    def set_button_color(movie):
        """Set color code depending on movie.is_watched."""
        display_color = UN_WATCHED_COLOR
        if movie.is_watched:
            display_color = WATCHED_COLOR
        return display_color

    def handle_press_movie(self, instance):
        """Handle pressing movie buttons."""
        # toggle watched / un watched
        if instance.movie.is_watched:
            instance.movie.un_watch_movie()
        else:
            instance.movie.watch_movie()
        # update button colour
        instance.background_color = self.set_button_color(instance.movie)
        # update status text
        unwatched_string = 'need to watch'
        if instance.movie.is_watched:
            unwatched_string = 'have watched'
        # Change status text if movie is unwatched
        self.status_text = "You {} {}".format(unwatched_string, instance.movie.title)
        instance.text = self.display_watched(instance.movie)
        self.update_movie_buttons()
        # update movies to watch text
        self.movies_to_watch_text = "To watch: {} Watched: {}".format(self.movie_collection.get_number_un_watched(),
                                                                      self.movie_collection.get_number_watched())

    def change_spinner_selection(self, new_sort_selection):
        """Handle changing spinner sort condition."""
        self.current_selection = new_sort_selection
        self.update_movie_buttons()

    def update_movie_buttons(self):
        """Update movie button order in GUI."""
        self.movie_collection.sort_movies(SPINNER_OPTIONS_TO_KEYWORD[self.current_selection])
        self.root.ids.entries_box.clear_widgets()
        self.create_widgets()

    def handle_press_add_movie(self, new_title, new_year, new_category):
        """Handle adding a new movie object."""
        if self.is_valid_inputs(new_title, new_year, new_category):
            self.movie_collection.add_movie(Movie(new_title, int(new_year), new_category, False))
            # create a button for new movie
            temp_button = Button(text="{} ({} from {})".format(new_title, new_category, new_year), id=new_title,
                                 background_color=UN_WATCHED_COLOR)
            temp_button.bind(on_release=self.handle_press_movie)
            # Store a reference to the movie object in the button object
            temp_button.movie = self.movie_collection.movies[-1]
            # clear text fields in entry boxes
            self.clear_fields()
            self.update_movie_buttons()

    def is_valid_inputs(self, title, year, category):
        """Check if user inputs meet requirements."""
        input_fields = [title, year, category]
        # check no empty input fields
        for field in input_fields:
            if field == '':
                self.status_text = "All fields must be completed"
                return False
        # check year is a number
        try:
            year = int(year)
        except ValueError:
            self.status_text = "Please enter a valid number"
            return False
        # check year is >=0
        if not year >= 0:
            self.status_text = "Year must be >=0"
            return False
        # check valid category
        valid_category_options = ["Action", "Comedy", "Documentary", "Drama", 'Fantasy', 'Thriller']
        if category not in valid_category_options:
            self.status_text = "Category must be one of Action, Comedy, Documentary, Drama, Fantasy, Thriller"
            return False
        return True

    def clear_fields(self):
        """Clear text inputs and status bar on press."""
        self.root.ids.new_title.text = ''
        self.root.ids.new_year.text = ''
        self.root.ids.new_category.text = ''
        self.status_text = ''

    @staticmethod
    def display_watched(instance):
        """Display 'watched' after titles that have been watched."""
        watched_string = 'watched'
        if not instance.is_watched:
            watched_string = ''
        button_display_text = instance.text = "{} ({} from {}) {}".format(instance.title, instance.category,
                                                                          instance.year, watched_string)
        return button_display_text

    def on_stop(self):
        """Run when the app exits and save movies to file."""
        self.movie_collection.bool_to_status()
        self.movie_collection.save_movies(FILE_NAME)


if __name__ == '__main__':
    MoviesToWatchApp().run()
