from model.user import User
from model.movie_5 import Movie5
#from selenium_fixture import app


def test_add_movie(app):
    app.ensure_login_as(User.Admin())
    app.add_movie(Movie5.Gatsby())
    app.add_movie(Movie5.Titanic())
    app.logout()
