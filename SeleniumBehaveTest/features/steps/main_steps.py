import time
from behave import *
from yaml import load
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
# Login feature

@given('url address "{text}"')
def step_impl(context, text):
    context.settings = load(open('features\conf.yaml').read())
    url = context.settings['base_url']
    basic_url = 'https://{}/'.format(url)
    if 'staging' in url or 'dev' in url:
        context.browser.get(basic_url)
    context.browser.get('https://{}/'.format(url)+text)
    time.sleep(3)


@when('user enters a username "{user_name}"')
def step_impl(context, user_name):
    xpath_username_field = "//*[@id='username']"
    context.browser.find_element_by_xpath(xpath_username_field).send_keys(user_name)


@step('user enters a password "{password}"')
def step_impl(context, password):
    xpath_password_field = "//*[@id='password']"
    context.browser.find_element_by_xpath(xpath_password_field).send_keys(password)


@step("click Login button")
def step_impl(context):
   xpath_login_button = "//*[@id='loginbtn']"
   context.browser.find_element_by_xpath(xpath_login_button).click()


@then('I should have a title "{title_test}"')
def step_impl(context, title_test):
    def step_impl(context, title_test):
        # I can use also less complicated way like "//*[text()='et.erickson.it: Expert Teacher']"
        xpath_title_text = "//*[conteins(text()='et.erickson.it: Expert Teacher')]"
        actual_massage = context.browser.find_element_by_xpath(xpath_title_text).text
        assert actual_massage == title_test



# Login feature with invalid credential
@then('I should have a message "{expected_errore_message}"')
def step_impl(context, expected_errore_message):
    xpath_errore_message = "//*[@id='loginerrormessage']"
    actual_result = context.browser.find_element_by_xpath(xpath_errore_message).text
    assert actual_result == expected_errore_message



# Select on drop down menu "English (en) language"
# @when("user navigate to drop down language menu")
# def step_impl(context):
#   xpath_menu_language_dropdown = "//*[@class='custom-select langmenu']"
#   dropdown_language_menu = context.browser.find_element_by_xpath(xpath_menu_language_dropdown)
#   # WebDriverWait(context, 3)
#   action = ActionChains(context.browser)
#   action.move_to_element(dropdown_language_menu)

@when("user navigate to drop down language menu")
def step_impl(context):
  xpath_menu_language_dropdown = "//*[@class='custom-select langmenu']"
  dropdown_language_menu = context.browser.find_element_by_xpath(xpath_menu_language_dropdown).click()


@step("select English (en) language")
def step_impl(context):
 xpath_english_language = "//option[@value='en']"
 time.sleep(3)
 context.browser.find_element_by_xpath(xpath_english_language).click()


# @then('User should has the page log in in "English" language')
# def step_impl(context):
