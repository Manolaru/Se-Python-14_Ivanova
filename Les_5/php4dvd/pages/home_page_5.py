from internal_page import InternalPage
from php4dvd.pages.blocks.user_form import UserForm
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class HomePage5(InternalPage):

    @property
    def add_movie_button(self):
        return self.driver.find_element_by_css_selector('img[alt="Add movie"]')

    @property
    def search_field(self):
        return self.driver.find_element_by_id("q")

    # @property
    def no_movies(self):
        return self.driver.find_element_by_css_selector('div[class="content"]')

    # @property
    def movie(self, name):
        return self.driver.find_element_by_css_selector('div[alt="' + name + '"]')

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, "nav"))
