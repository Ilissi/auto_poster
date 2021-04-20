from BaseRedditPage import BaseRedditPage
from selenium.webdriver.common.by import By

class TwitterSearchLocator:
    LOCATOR_USERNAME = (By.XPATH, "//input[@name='username']")
    LOCATOR_PASSWORD = (By.XPATH, "//input[@name='password']")
    LOCATOR_ENTER = (By.XPATH, "//button[@class='AnimatedForm__submitButton m-full-width']")
    FIND_FIELD = (By.XPATH, "//input[@placeholder='Create Post']")

class SearchHelper(BaseRedditPage):

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

    def click_on_the_field(self):
        return self.find_element()