from internal_page import InternalPage
from php4dvd.pages.blocks.user_form import UserForm
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class UserManagementPage(InternalPage):

    def __init__(self, driver, base_url):
        super(UserManagementPage, self).__init__(driver, base_url)
        self.user_form = UserForm(self.driver, self.base_url)

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, "nav"))

    # more page elements here