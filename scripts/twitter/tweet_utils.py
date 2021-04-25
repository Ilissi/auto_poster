import time
from twitter.LoginPage import SearchHelper

def tweeted(browser, username, password, title, phone_number):
    try:
        twitter_login_page = SearchHelper(browser)
        twitter_login_page.go_to_site()
        twitter_login_page.enter_username(username)
        twitter_login_page.enter_password(password)
        twitter_login_page.click_on_the_login_button()
        time.sleep(2)
        twitter_login_page.security(phone_number)
        twitter_login_page.send_tweet(title)
        time.sleep(3)
        twitter_login_page.click_on_the_tweet_button(title)
    except:
        print('Something happened with posted of twitter')
        twitter_login_page.quit1()



