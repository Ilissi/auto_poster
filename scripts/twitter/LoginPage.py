from BaseTwitterPage import BaseTwitterPage
from selenium.webdriver.common.by import By

class TwitterSearchLocator:
    LOCATOR_USERNAME = (By.XPATH, "//input[@name='session[username_or_email]']")
    LOCATOR_PASSWORD = (By.XPATH, "//input[@name='session[password]']")
    LOCATOR_ENTER = (By.XPATH, "//span[text()='Log in']")

class SearchHelper(BaseTwitterPage):

    def enter_username(self, username):
        search_field = self.find_element(TwitterSearchLocator.LOCATOR_USERNAME)
        search_field.click()
        search_field.send_keys(username)
        return search_field

    def enter_password(self, password):
        search_field = self.find_element(TwitterSearchLocator.LOCATOR_PASSWORD)
        search_field.click()
        search_field.send_keys(password)
        return search_field

    def click_on_the_login_button(self):
        return self.find_element(TwitterSearchLocator.LOCATOR_ENTER, time=2).click()