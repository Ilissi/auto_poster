import time
from scripts.reddit.LoginPage import SearchHelper


def reddited(browser, username, password, community, title, description, urls, image, tag):
    try:
        reddit_login_page = SearchHelper(browser)
        reddit_login_page.go_to_site()
        reddit_login_page.enter_username(username)
        reddit_login_page.enter_password(password)
        reddit_login_page.click_on_the_login_button()
        time.sleep(5)
        reddit_login_page.click_on_the_field()
        time.sleep(5)
        reddit_login_page.send_reddit_post(community, title, description, urls, image, tag)
        time.sleep(10)
        reddit_login_page.send_post()
        time.sleep(5)

    except:
        print('Something happened with posted of reddit')
        reddit_login_page.quit()

