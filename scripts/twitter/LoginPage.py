import time

from twitter.BaseTwitterPage import BaseTwitterPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TwitterSearchLocator:
    LOCATOR_USERNAME = (By.XPATH, "//input[@name='session[username_or_email]']")
    LOCATOR_PASSWORD = (By.XPATH, "//input[@name='session[password]']")
    LOCATOR_ENTER_EN = (By.XPATH, "//span[text()='Log in']")
    LOCATOR_ENTER_RU = (By.XPATH, "//span[text()='Войти']")
    LOCATOR_TEXT_FIELD = (By.XPATH,  "//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")
    LOCATOR_SEND_TWEET = (By.XPATH, "//span[@class='css-901oao css-16my406 css-bfa6kz r-poiln3 r-bcqeeo r-qvutc0']//span[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][contains(text(),'Tweet')]")

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
        return self.find_element(TwitterSearchLocator.LOCATOR_ENTER_EN, time=2).click()

    def send_tweet(self, title):
        send_title = self.send_keys_tweet(TwitterSearchLocator.LOCATOR_TEXT_FIELD, title)
        send_title = self.send_keys_tweet(TwitterSearchLocator.LOCATOR_TEXT_FIELD, Keys.RETURN)
        return send_title

    def click_on_the_tweet_button(self):
        first_of_all = self.find_element(TwitterSearchLocator.LOCATOR_SEND_TWEET, time=2).click()
        time.sleep(2)
        return self.quit()

    def excep(self):
        return self.do_screen()



