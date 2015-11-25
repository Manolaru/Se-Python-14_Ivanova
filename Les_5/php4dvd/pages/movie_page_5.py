from internal_page import InternalPage
from php4dvd.pages.blocks.user_form import UserForm
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class MoviePage5(InternalPage):

    @property
    def edit_button(self):
        return self.driver.find_element_by_css_selector("img[alt=\"Edit\"]")

    @property
    def remove_button(self):
        return self.driver.find_element_by_css_selector("img[alt=\"Remove\"]")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, "img[alt=\"Remove\"]"))

