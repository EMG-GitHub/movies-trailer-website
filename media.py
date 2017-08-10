# Import webbrowser so that show_trailer instance method works.
import webbrowser


# Create a data structure which allows to create multiple instantces of itself.
# Python Class: Movie, Google style guide for Python suggests uppercase.
# It is good practice to have the class definition in one file and call/use
# it from another files.

class Movie():
    """This class provides a way to store movie related information"""

    """Function __init__ is called, initializes/creates space in memory
       for each new instance.
       Also called Contructor (where the argument self would point
       to the instance being created)."""

    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
            # Instance variables:
            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube

    # Define instance method,
    # function that will open a browser and
    # play the trailer passed as value in instance variables.

    def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)
