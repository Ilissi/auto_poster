import time
from twitter.LoginPage import SearchHelper

def tweeted(browser, username, password, title):
    try:
        twitter_login_page = SearchHelper(browser)
        twitter_login_page.go_to_site()
        twitter_login_page.enter_username(username)
        twitter_login_page.enter_password(password)
        twitter_login_page.click_on_the_login_button()
        twitter_login_page.send_tweet(title)
        time.sleep(5)
        twitter_login_page.excep()
        twitter_login_page.click_on_the_tweet_button()
    except:
        print('Something wrong with twitter')

