# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class LisaysE(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_lisays_e(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()

        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_id("submit").click() # 'Save' button
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("Pirates")
        driver.find_element_by_id("submit").click() # 'Save' button
        driver.find_element_by_name("aka").clear()
        driver.find_element_by_name("aka").send_keys("pirates")
        driver.find_element_by_name("duration").clear()
        driver.find_element_by_name("duration").send_keys("120")
        driver.find_element_by_id("own_no").click()
        driver.find_element_by_id("seen_no").click()
        driver.find_element_by_id("cover").clear()
        driver.find_element_by_id("cover").send_keys("C:\\Users\\Katja\\Pictures\\testaus kurssi\\pirates.jpg")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_id("text_languages_0").clear()
        driver.find_element_by_id("text_languages_0").send_keys("English")
        driver.find_element_by_name("subtitles").clear()
        driver.find_element_by_name("subtitles").send_keys("French")
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys("2004")
        driver.find_element_by_id("submit").click() # 'Save' button
        driver.find_element_by_link_text("Home").click()

        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_id("submit").click() # 'Save' button
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("Hilton")
        driver.find_element_by_id("submit").click() # 'Save' button
        driver.find_element_by_name("aka").clear()
        driver.find_element_by_name("aka").send_keys("jotakin")
        driver.find_element_by_id("seen_no").click()
        driver.find_element_by_id("cover").clear()
        driver.find_element_by_id("cover").send_keys("C:\\Users\\Katja\\Pictures\\testaus kurssi\\Horizon.jpg")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_id("submit").click()
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys("1978")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_link_text("Home").click()

        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_id("submit").click() # 'Save' button
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("Gatsby")
        driver.find_element_by_id("submit").click() # 'Save' button
        driver.find_element_by_name("aka").clear()
        driver.find_element_by_name("aka").send_keys("about")
        driver.find_element_by_id("loaned_yes").click()
        driver.find_element_by_id("loaned_yes").click()
        driver.find_element_by_id("cover").clear()
        driver.find_element_by_id("cover").send_keys("C:\\Users\\Katja\\Pictures\\testaus kurssi\\Gatsby.jpg")
        driver.find_element_by_name("taglines").clear()
        driver.find_element_by_name("taglines").send_keys("axxaxa")
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys("2000")

        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()



        # driver.find_element_by_name("aka").clear()
        # driver.find_element_by_name("aka").send_keys("about")

        # driver.find_element_by_id("loaned_yes").click()
        # driver.find_element_by_id("loaned_yes").click()
        # driver.find_element_by_id("cover").clear()
        # driver.find_element_by_id("cover").send_keys("C:\\Users\\Katja\\Pictures\\testaus kurssi\\Gatsby.jpg")
        # driver.find_element_by_name("taglines").clear()
        # driver.find_element_by_name("taglines").send_keys("axxaxa")
        # driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        # driver.find_element_by_id("submit").click()


        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_link_text("Log out").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to log out[\s\S]$")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True

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

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
