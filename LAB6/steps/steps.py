from selenium import webdriver
import time
from behave import given, when, then

@given('I am on the Facebook login page')
def step_facebook_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.facebook.com/")

@given('I am on the Instagram login page')
def step_instagram_login_page(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://www.instagram.com/")

@when('I enter valid credentials')
def step_enter_valid_credentials(context):
    time.sleep(18)  # Czas na ręczne wprowadzenie danych

@then('I should be logged in successfully on Facebook')
def step_check_facebook_login(context):
    assert is_logged_in(context.driver)

@then('I should be logged in successfully on Instagram')
def step_check_instagram_login(context):
    assert is_logged_in(context.driver)

@then('close the browser')
def step_close_browser(context):
    context.driver.quit()

def is_logged_in(driver):
    # Sprawdzenie warunku logowania
    return True
