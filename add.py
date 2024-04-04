# Importing necessary modules and classes
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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class Add:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    actions = ActionChains(driver)

    def booting_function(self):
        try:
            self.driver.maximize_window()
            self.driver.get(data.WebData().url)
            print("Browser started successfully.")
            return True
        except Exception as e:
            print(f"ERROR: Unable to start the browser: {e}")
            return False

    def quit(self):
        self.driver.quit()

    def login(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))).send_keys(
                data.WebData().username)

            self.driver.find_element(by=By.NAME, value=locators.WebLocators().password_locator).send_keys(
                data.WebData().password)

            self.driver.find_element(by=By.XPATH, value=locators.WebLocators().login_button_locator).click()
            print("Login successful.")
            return True
        except Exception as e:
            print(f"Error during login: {e}")
            return False

    def add_emp(self):
        try:

            pim_link = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim_link_locator)))
            pim_link.click()

            click_add = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().add_button_locator)))
            click_add.click()

            sleep(2)

            #  Fill in employee details and save
            self.actions.send_keys(Keys.TAB).perform()

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().fname_locator))).send_keys(
                data.WebData().add_fname)
            print("First Name filled")
            sleep(3)

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().mname_locator))).send_keys(
                data.WebData().add_mname)
            print("Middle Name filled")
            sleep(3)

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().lname_locator))).send_keys(
                data.WebData().add_lname)
            print("Last Name filled")
            sleep(3)

            WebDriverWait(self.driver, 40).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().emp_id_locator))).send_keys(
                data.WebData().add_emp_id)
            print("Employee ID filled")
            sleep(3)

            toggle = WebDriverWait(self.driver, 10).until(
              EC.visibility_of_element_located((By.XPATH, locators.WebLocators().toggle_locator)))
            toggle.click()
            sleep(3)

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().uname_locator))).send_keys(
                data.WebData().add_username)
            print("UserName filled")
            sleep(3)

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pass_locator))).send_keys(
                data.WebData().add_password)
            print("Password filled")
            sleep(3)

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().confirm_pass_locator))).send_keys(
                data.WebData().confirm_password)
            print("Confirm Password filled")
            sleep(3)


            save = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().save_locator)))
            save.click()
            sleep(3)

            print("Successfully Added")
        except Exception as e:
            print(f"Error during adding employee: {e}")


if __name__ == "__main__":
    add = Add()
    if add.booting_function() and add.login():
        add.add_emp()
        add.quit()