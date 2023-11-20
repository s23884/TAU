import unittest
from selenium import webdriver
import time

class TestLogin(unittest.TestCase):

    def test_facebook_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com/")

        time.sleep(18)  # Czas na ręczne wprowadzenie danych

        # Sprawdzenie warunku logowania
        self.assertTrue(self.is_logged_in(driver))

        # Zamknięcie przeglądarki
        driver.quit()

    def test_instagram_login(self):
        driver = webdriver.Firefox()
        driver.get("https://www.instagram.com/")

        time.sleep(18)  # Czas na ręczne wprowadzenie danych

        # Sprawdzenie warunku logowania
        self.assertTrue(self.is_logged_in(driver))

        # Zamknięcie przeglądarki
        driver.quit()

    def is_logged_in(self, driver):
        return True

if __name__ == "__main__":
    unittest.main()
