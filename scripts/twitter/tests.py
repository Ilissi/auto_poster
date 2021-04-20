import time

from selenium import webdriver
from LoginPage import SearchHelper

def do_login(browser, username, password, title):
    twitter_login_page = SearchHelper(browser)
    twitter_login_page.go_to_site()
    twitter_login_page.enter_username(username)
    twitter_login_page.enter_password(password)
    twitter_login_page.click_on_the_login_button()
    twitter_login_page.send_tweet(title)
    time.sleep(5)
    twitter_login_page.click_on_the_tweet_button()
    time.sleep(5)

def main():
    browser = webdriver.Chrome(executable_path='/Users/maksimboginic/PycharmProjects/upwork_auto_poster_selenium/auto_poster/chromedriver')
    username = '+380689811801'
    password = 'Vick1715'
    do_login(browser, username, password, 'Lady jasoos web series EP3\nBhahi banged! nude all alone inside Beauty bed harder into night dree\nhttps://4kporn.xxx/videos/130315/lady-jasoos-web-series-ep3/?utm_source=reddit&utm_medium=plugs&utm_campaign=username\n#fuck_harder #fucking #hot_fuck #hottest #ladies #lady #naked_fuck #series #web #web_series #one_night #in_bed #la_e #banged_hard #hard_bang #hard_inside #hard')

if __name__ == '__main__':
    main()
