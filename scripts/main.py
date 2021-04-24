#!/usr/bin/python3
import jsoncfg
from selenium import webdriver


from reddit import reddit_utils
from twitter import tweet_utils
from utils import get_xml

def main():
    config = jsoncfg.load_config('/home/adminroot/autoposter/auto_poster/scripts/config.cfg')
    chrome_options = webdriver.ChromeOptions()
    if config.proxies() != "":
        chrome_options.add_argument('--proxy-server=%s' % config.proxies)
    #initialize WebDriverSession

    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--disable-dev-shm-usage')

    url_xml = config.url_for_parse()

    for twitter_user in config.twitter_users():
        xlm_list = get_xml.get_list(url_xml)
        for urls_data in xlm_list[:-1]:
            browser = webdriver.Chrome(
                executable_path=config.SeleniumPath(),
                chrome_options=chrome_options)
            data_for_post = get_xml.string_to_send_tweet(urls_data)
            tweet_utils.tweeted(browser, twitter_user['username'], twitter_user['password'], data_for_post)

    for reddit_user in config.reddit_users():
        xlm_list = get_xml.get_list(url_xml)
        for urls_data in xlm_list[:-1]:
            browser = webdriver.Chrome(
                executable_path=config.SeleniumPath(),
                chrome_options=chrome_options)
            data_for_post = get_xml.string_to_dict_post_reddit(urls_data, config.DirForSave())
            reddit_utils.reddited(browser, reddit_user['username'], reddit_user['password'], reddit_user['reddit_community'], data_for_post['title'], data_for_post['description'],
                     data_for_post['url'], data_for_post['img_path'], data_for_post['tags'])





if __name__ == '__main__':
    main()