import webbrowser
class Movie():
    """this class is about creating a movie website"""
    VALID_RATINGS = ['A+','B','1st','B grade'] #class variable acc to google styleguide
    def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image = movie_poster
        self.trailer = movie_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
    def show_poster(self):
        webbrowser.open(self.poster_image)
