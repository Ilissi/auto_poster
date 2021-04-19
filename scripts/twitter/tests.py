from LoginPage import SearchHelper

def do_login(browser, username, password):
    twitter_login_page = SearchHelper(browser)
    twitter_login_page.go_to_site()
    twitter_login_page.enter_username(username)
    twitter_login_page.enter_password(password)
    twitter_login_page.click_on_the_login_button()