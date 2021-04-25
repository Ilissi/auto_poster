import time

from twitter.BaseTwitterPage import BaseTwitterPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TwitterSearchLocator:
    LOCATOR_USERNAME = (By.XPATH, "//input[@name='session[username_or_email]']")
    LOCATOR_PASSWORD = (By.XPATH, "//input[@name='session[password]']")
    LOCATOR_ENTER_EN = (By.XPATH, "//span[text()='Log in']")
    LOCATOR_ENTER_RU = (By.XPATH, "//span[text()='Войти']")
    LOCATOR_ENTER_SECURITY = (By.XPATH, "//input[@id='challenge_response']")
    LOCATOR_ENTER_SECURITY_BUTTON = (By.XPATH, "//input[@id='email_challenge_submit']")
    LOCATOR_TEXT_FIELD = (By.XPATH,  "//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")
    #LOCATOR_ADD_TW = (By.XPATH,  "//div[@aria-label='Tweet text']")
    LOCATOR_SEND_TWEET = (By.XPATH,  "//span[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][contains(text(),'Tweet')]")
    LOCATOR_SEND_TWEET_1 = (By.XPATH, "//span[@class='css-901oao css-16my406 css-bfa6kz r-poiln3 r-bcqeeo r-qvutc0']//span[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][contains(text(),'Tweet')]")

class SearchHelper(BaseTwitterPage):

    def enter_username(self, username):
        search_field = self.find_element(TwitterSearchLocator.LOCATOR_USERNAME)
        search_field.click()
        search_field.send_keys(username)
        time.sleep(2)
        return search_field

    def enter_password(self, password):
        search_field = self.find_element(TwitterSearchLocator.LOCATOR_PASSWORD)
        search_field.click()
        search_field.send_keys(password)
        time.sleep(2)
        return search_field

    def click_on_the_login_button(self):
        return self.find_element(TwitterSearchLocator.LOCATOR_ENTER_EN, time=2).click()

    def send_tweet(self, title):
        send_title = self.send_keys_tweet(TwitterSearchLocator.LOCATOR_TEXT_FIELD, title)
        send_title = self.send_keys_tweet(TwitterSearchLocator.LOCATOR_TEXT_FIELD, Keys.RETURN)
       # return self.find_element(TwitterSearchLocator.LOCATOR_ADD_TW, time=2).click()

    def click_on_the_tweet_button(self, keys_for_enter):

        lol = self.find_element(TwitterSearchLocator.LOCATOR_SEND_TWEET_1).click()
        self.send_tweet(keys_for_enter)
        return self.find_element(TwitterSearchLocator.LOCATOR_SEND_TWEET_1).click()

    def click_on_the_tweet(self):
        return self.click_(TwitterSearchLocator.LOCATOR_SEND_TWEET_1)

    def quit1(self):
        return self.quit()

    def security(self, phone_number):
        try:
            enter_number = self.find_element(TwitterSearchLocator.LOCATOR_ENTER_SECURITY, time=2)
            enter_number.click()
            enter_number.send_keys(phone_number)
            return self.find_element(TwitterSearchLocator.LOCATOR_ENTER_SECURITY_BUTTON, time=2).click()
        except:
            pass

    def excep(self):
        return self.do_screen()



