import time
from behave import *
from time import sleep
from yaml import load
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

# wait = WebDriverWait(browser, 5)
# try:
#     page_loaded = wait.until_not(
#         lambda browser: browser.current_url == login_page
#     )
# except TimeoutException:
#     self.fail("Loading timeout expired")
#
# self.assertEqual(
#     browser.current_url,
#     correct_page,
#     msg="Successful Login"
# )

# Login feature

@given('url address "{text}"')
def step_impl(context, text):
    context.settings = load(open('features\conf.yaml').read())
    url = context.settings['base_url']
    basic_url = 'https://{}/'.format(url)
    if 'staging' in url or 'dev' in url:
        context.browser.get(basic_url)
    context.browser.get('https://{}/'.format(url) + text)
    time.sleep(2)



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


# Login feature with invalid credential__________________________________________________________________________________
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
#   action.move_to_element_with_offset(dropdown_language_menu)

@when("user navigate to drop down language menu")
def step_impl(context):
    xpath_menu_language_dropdown = "//*[@class='custom-select langmenu']"
    dropdown_language_menu = context.browser.find_element_by_xpath(xpath_menu_language_dropdown).click()


@step("select English (en) language")
def step_impl(context):
    xpath_english_language = "//option[@value='en']"
    time.sleep(2)
    context.browser.find_element_by_xpath(xpath_english_language).click()

@then('User should has the page log-in in "{expected_result}" language')
def step_impl(context, expected_result):
    xpath_language_page = "//option[@value='en']"
    actual_result = context.browser.find_element_by_xpath(xpath_language_page).text
    time.sleep(2)
    if actual_result == 0:
        assert print(expected_result)

# lateralBlock.feature___________________________________________________________________________________________________
# /login in one step----------------------------------------------------------------------------------------------------
@given('set up url address "{text}"')
def step_impl(context, text):
    context.settings = load(open('features\conf.yaml').read())
    url = context.settings['base_url']
    basic_url = 'https://{}/'.format(url)
    if 'staging' in url or 'dev' in url:
        context.browser.get(basic_url)
    context.browser.get('https://{}/'.format(url) + text)
    time.sleep(2)
    username ="i.senkiv"
    password = "Totara_2019"
    xpath_username_field = "//*[@id='username']"
    context.browser.find_element_by_xpath(xpath_username_field).send_keys(username)
    xpath_password_field = "//*[@id='password']"
    context.browser.find_element_by_xpath(xpath_password_field).send_keys(password)
    xpath_login_button = "//*[@id='loginbtn']"
    context.browser.find_element_by_xpath(xpath_login_button).click()
    time.sleep(3)


# user closes lateral menu for view home page in full screen_______________________________________________________________-
@step("click on the button of the lateral menu")
def step_impl(context):
    button = context.browser.find_element_by_xpath("//*[@class='fas fa-chevron-left']")
    context.browser.execute_script("arguments[0].click();", button)
    time.sleep(3)

@then("lateral menu should be closed")
def step_impl(context):
    time.sleep(3)
    try:
        datamt_status_close = context.browser.find_element_by_xpath("//body[@data-mtstatus='notmttoggled']")
        print("Lateral menu is closed")
    except:
        print("The xpath is invalid")
