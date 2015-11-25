from model.user import User
from model.movie_5 import Movie5
#from selenium_fixture import app


def test_remove_movie(app):
    app.ensure_login_as(User.Admin())
    app.remove_movie(Movie5.Titanic().name)
    app.remove_movie(Movie5.Gatsby().name)
    app.logout()
