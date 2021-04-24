import time

from reddit.BaseRedditPage import BaseRedditPage
from selenium.webdriver.common.by import By

from utils import get_xml

class RedditSearchLocator:
    LOCATOR_USERNAME = (By.XPATH, "//input[@name='username']")
    LOCATOR_PASSWORD = (By.XPATH, "//input[@name='password']")
    LOCATOR_ENTER = (By.XPATH, "//button[@class='AnimatedForm__submitButton m-full-width']")
    FIND_FIELD = (By.XPATH, "//input[@placeholder='Create Post']")
    LOCATOR_COMMUNITY = (By.XPATH, "//input[@placeholder='Choose a community']")
    LOCATOR_TITLE = (By.XPATH, "//textarea[@placeholder='Title']")
    LOCATOR_IMAGE = "//input[@accept='image/png,image/gif,image/jpeg']"
    LOCATOR_TEXTBOX = (By.XPATH, "//div[@role='textbox']")
    LOCATOR_POST = (By.XPATH, "//button[@class='_18Bo5Wuo3tMV-RDB8-kh8Z _2iuoyPiKHN3kfOoeIQalDT _10BQ7pjWbeYP63SAPNS8Ts HNozj_dKjQZ59ZsfEegz8 ']")

class SearchHelper(BaseRedditPage):

    def enter_username(self, username):
        search_field = self.find_element(RedditSearchLocator.LOCATOR_USERNAME)
        search_field.click()
        search_field.send_keys(username)
        return search_field

    def enter_password(self, password):
        search_field = self.find_element(RedditSearchLocator.LOCATOR_PASSWORD)
        search_field.click()
        search_field.send_keys(password)
        return search_field

    def click_on_the_login_button(self):
        return self.find_element(RedditSearchLocator.LOCATOR_ENTER, time=2).click()

    def click_on_the_field(self):
        return self.find_element(RedditSearchLocator.FIND_FIELD, time=20).click()

    def send_reddit_post(self, community, title, description, urls, image, tag):
        send_community = self.send_keys_reddit(RedditSearchLocator.LOCATOR_COMMUNITY, community)
        send_title = self.send_keys_reddit(RedditSearchLocator.LOCATOR_TITLE, title)
        send_text_field = self.send_keys_reddit(RedditSearchLocator.LOCATOR_TEXTBOX, get_xml.string_joiner(description, urls, tag))
        time.sleep(1)
        try:
            send_image = self.send_key_image(RedditSearchLocator.LOCATOR_IMAGE, image)
        except: print('Image not required')

    def send_post(self):
        firs_of_all = self.find_element(RedditSearchLocator.LOCATOR_POST, time=2).click()
        time.sleep(10)
        return self.quit()
