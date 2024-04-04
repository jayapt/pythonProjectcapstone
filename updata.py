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


class Edit:
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
                EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))
            )
            self.driver.find_element(by=By.NAME, value=locators.WebLocators().username_locator).send_keys(
                data.WebData().username
            )

            self.driver.find_element(by=By.NAME, value=locators.WebLocators().password_locator).send_keys(
                data.WebData().password
            )

            self.driver.find_element(by=By.XPATH, value=locators.WebLocators().login_button_locator).click()
            print("Login successful.")
            return True
        except Exception as e:
            print(f"Error during login: {e}")
            return False

    def edit_emp(self):
        try:
            pim_link = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim_link_locator)))
            pim_link.click()

            employee_link = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().employee_link_locator)))
            employee_link.click()
            print("Employee List is loaded.")

            edit_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().edit_button_locator)))
            edit_button.click()
            print("Edit Button clicked")

            self.actions.send_keys(Keys.TAB).perform()

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().form_locator)))

            first_name = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().first_name_locator)))
            first_name.clear()
            first_name.send_keys("NewFirstName")
            print("F Name is edited.")
            sleep(3)

            middle_name = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().middle_name_locator)))
            middle_name.clear()
            middle_name.send_keys("NewMidddleName")
            print("MName is edited.")
            sleep(3)

            self.driver.find_element(By.XPATH, locators.WebLocators().last_name_locator).clear()
            self.driver.find_element(By.XPATH, locators.WebLocators().last_name_locator).send_keys("NewLastName")
            print("LName is edited.")
            sleep(2)

            self.driver.find_element(By.XPATH, locators.WebLocators().employee_id_locator).clear()
            self.driver.find_element(By.XPATH, locators.WebLocators().employee_id_locator).send_keys("120347")
            sleep(2)

            self.driver.find_element(By.XPATH, locators.WebLocators().other_id_locator).clear()
            self.driver.find_element(By.XPATH, locators.WebLocators().other_id_locator).send_keys("id")
            sleep(2)

            # Save the changes
            save= WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().save_button_locator)))
            save.click()
            sleep(2)
            save_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().save_button_locator2)))
            save_button.click()
            sleep(2)

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    edit = Edit()
    if edit.booting_function() and edit.login():
        edit.edit_emp()
        edit.quit()
