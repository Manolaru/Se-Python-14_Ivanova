from internal_page import InternalPage
from php4dvd.pages.blocks.movie_edit_form_5 import MovieEditForm5
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class MovieEditPage5(InternalPage):

    def __init__(self, driver, base_url):
        super(MovieEditPage5, self).__init__(driver, base_url)
        self.movie_edit_form = MovieEditForm5(self.driver, self.base_url)

    @property
    def save_button(self):
        return self.find_element_by_css_selector('img[alt="Save"]')

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, 'img[alt="Save"]'))
