import webbrowser


class Movie():
    """This class provides a way to store movie related information"""
    # Static Class Variable
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, movie_details, poster_image, trailer_youtube):  # noqa
        self.title = movie_title
        self.storyline = movie_storyline
        self.details = movie_details
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Function to open the trailer of a movie in the browser"""
        webbrowser.open(self.trailer_youtube_url)

    def show_details(self):
        """Function to open the IMDB site of the movie"""
        webbrowser.open(self.details)
