from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BaseRedditPage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.reddit.com/login/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def send_key_image(self, locator, keys_for_enter):
        uploadElement = self.driver.find_element_by_xpath(locator)
        return uploadElement.send_keys(keys_for_enter)

    def send_keys_reddit(self, locator, keys_for_enter, time=20):
        autotw1 = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located
            (locator), message=f"Can't find elements by locator {locator}")
        return ActionChains(self.driver).move_to_element(autotw1).click(autotw1).send_keys(keys_for_enter).perform()

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def quit(self):
        return self.driver.quit()

