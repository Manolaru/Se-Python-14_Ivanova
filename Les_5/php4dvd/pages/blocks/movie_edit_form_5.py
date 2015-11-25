from php4dvd.pages.page import Page
from selenium.webdriver.support.select import Select


class MovieEditForm5(Page):

    @property
    def name_field(self):
        return self.driver.find_element_by_name("name")

    @property
    def year_field(self):
        return self.driver.find_element_by_name("year")

    @property
    def duration_field(self):
        return self.driver.find_element_by_name("duration")

    @property
    def owner_select(self):
        return self.driver.find_element_by_id("own_no")

    @property
    def save_button(self):
        return self.driver.find_element_by_id("submit")
