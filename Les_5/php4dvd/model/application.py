import time

from php4dvd.model.user import User
from php4dvd.pages.internal_page import InternalPage
from php4dvd.pages.login_page import LoginPage
from php4dvd.pages.user_management_page import UserManagementPage
from php4dvd.pages.user_profile_page import UserProfilePage
from php4dvd.pages.home_page_5 import HomePage5
from php4dvd.pages.movie_page_5 import MoviePage5
from php4dvd.pages.movie_edit_page_5 import MovieEditPage5

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class Application(object):
    def __init__(self, driver, base_url):
        driver.get(base_url)
        self.wait = WebDriverWait(driver, 10)
        self.login_page = LoginPage(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.user_profile_page = UserProfilePage(driver, base_url)
        self.user_management_page = UserManagementPage(driver, base_url)
        
        self.home_page = HomePage5(driver, base_url)
        self.movie_page = MoviePage5(driver, base_url)
        self.movie_edit_page = MovieEditPage5(driver, base_url)


    def logout(self):
        self.internal_page.logout_button.click()
        self.wait.until(alert_is_present()).accept()

    def ensure_logout(self):
        element = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "nav, #loginform")))
        if element.tag_name == "nav":
            self.logout()

    def login(self, user):
        lp = self.login_page
        lp.is_this_page
        lp.username_field.send_keys(user.username)
        lp.password_field.send_keys(user.password)
        lp.submit_button.click()

    def ensure_login_as(self, user):
        element = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "nav, #loginform")))
        if element.tag_name == "nav":
            # we are on internal page
            if self.is_logged_in_as(user):
                return
            else:
                self.logout()
        self.login(user)

    def is_logged_in(self):
        return self.home_page.is_this_page

    def is_logged_in_as(self, user):
        return self.is_logged_in() \
            and self.get_logged_user().username == user.username

    def is_not_logged_in(self):
        return self.login_page.is_this_page

    def get_logged_user(self):
        self.internal_page.user_profile_link.click()
        upp = self.user_profile_page
        upp.is_this_page
        return User(username=upp.user_form.username_field.get_attribute("value"),
                    email=upp.user_form.email_field.get_attribute("value"))

    def add_user(self, user):
        self.internal_page.user_management_link.click()
        ump = self.user_management_page
        ump.is_this_page
        ump.user_form.username_field.send_keys(user.username)
        ump.user_form.email_field.send_keys(user.email)
        ump.user_form.password_field.send_keys(user.password)
        ump.user_form.password1_field.send_keys(user.password)
        # ump.user_form.role_select.select_by_visible_text(user.role)
        ump.user_form.submit_button.click()

    def add_movie(self, movie):
        self.home_page.add_movie_button.click()
        mep = self.movie_edit_page
        mep.is_this_page
        mep.movie_edit_form.name_field.clear()
        mep.movie_edit_form.name_field.send_keys(movie.name)
        mep.movie_edit_form.year_field.clear()
        mep.movie_edit_form.year_field.send_keys(movie.year)
        mep.movie_edit_form.duration_field.clear()
        mep.movie_edit_form.duration_field.send_keys(movie.duration)
        # mep.movie_edit_form.owner_select.click(movie.owner)
        mep.movie_edit_form.save_button.click()
        mp = self.movie_page
        mp.is_this_page
        mp.home_link.click()
        self.home_page.is_this_page

    def remove_movie(self, name):
        self.home_page.movie(name).click()
        mp = self.movie_page
        mp.is_this_page
        mp.remove_button.click()
        mp.close_alert_and_get_its_text()
        self.home_page.is_this_page

    def search_existing(self, name):
        self.home_page.search_field.clear()
        self.home_page.search_field.send_keys(name+"\n")
        time.sleep(1)
        self.home_page.movie(name)
        self.home_page.search_field.clear()
        self.home_page.search_field.send_keys("\n")
        time.sleep(1)

    def search_missing(self, name):
        self.home_page.search_field.clear()
        self.home_page.search_field.send_keys(name+"\n")
        time.sleep(1)
        self.home_page.no_movies()
        self.home_page.search_field.clear()
        self.home_page.search_field.send_keys("\n")
        time.sleep(1)

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

