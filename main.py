from Data import data
from Locators import locators
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def start(self):
        self.driver.maximize_window()
        self.driver.get(data.WebData().url)

    def quit(self):
        self.driver.quit()

    def login(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))).send_keys(
                data.WebData().username)
            print("Entering username:", data.WebData().username)
            self.driver.find_element(by=By.NAME, value=locators.WebLocators().password_locator).send_keys(
                data.WebData().password)
            print("Entering password:", data.WebData().password)
            self.driver.find_element(by=By.XPATH, value=locators.WebLocators().login_button_locator).click()
            print("The user is logged in successfully")

        except NoSuchElementException as e:
            print("Error : ", e)
        finally:
            self.quit()


if __name__ == '__main__':
    login_page = Login()
    login_page.start()
    login_page.login()
    login_page.quit()