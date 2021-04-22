from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BaseTwitterPage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://twitter.com/login"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def send_keys_tweet(self, locator, keys_for_enter, time=10):
        autotw1 = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located
            (locator), message=f"Can't find elements by locator {locator}")
        return ActionChains(self.driver).move_to_element(autotw1).click(autotw1).send_keys(keys_for_enter).perform()

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def do_screen(self):
        return self.driver.get_screenshot_as_file("screenshot.png")

    def quit(self):
        return self.driver.quit()
