from model.user import User
from model.movie_5 import Movie5
#from selenium_fixture import app


def test_search_movie(app):
    app.ensure_login_as(User.Admin())
    app.add_movie(Movie5.Gatsby())
    app.add_movie(Movie5.Titanic())
    app.search_existing(Movie5.Gatsby().name)
    app.search_existing(Movie5.Titanic().name)
    app.search_missing(Movie5.Batman().name)
    app.remove_movie(Movie5.Titanic().name)
    app.remove_movie(Movie5.Gatsby().name)
    app.logout()
