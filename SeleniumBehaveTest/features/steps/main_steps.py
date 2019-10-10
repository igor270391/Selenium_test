import time
from behave import *
from time import sleep
from yaml import load
import sqlite3
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


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
    time.sleep(3)


@then('I should have a title "{title_test}"')
def step_impl(context, title_test):
    def step_impl(context, title_test):
        # I can use also less complicated way like "//*[text()='et.erickson.it: Expert Teacher']"
        xpath_title_text = "//*[contains(text()='et.erickson.it: Expert Teacher')]"
        actual_massage = context.browser.find_element_by_xpath(xpath_title_text).text
        assert actual_massage == title_test
        time.sleep(2)


# Login feature with invalid credential__________________________________________________________________________________
@then('I should have a message "{expected_errore_message}"')
def step_impl(context, expected_errore_message):
    xpath_errore_message = "//*[@id='loginerrormessage']"
    actual_result = context.browser.find_element_by_xpath(xpath_errore_message).text
    time.sleep(3)
    assert actual_result == expected_errore_message


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


# lateralBlock.feature__________________________________________________________________________________________________
# /login in one step----------------------------------------------------------------------------------------------------
@given('set up url address "{text}" and execute log in')
def step_impl(context, text):
    context.settings = load(open('features\conf.yaml').read())
    url = context.settings['base_url']
    basic_url = 'https://{}/'.format(url)
    if 'staging' in url or 'dev' in url:
        context.browser.get(basic_url)
    context.browser.get('https://{}/'.format(url) + text)
    time.sleep(2)
    username = "i.senkiv"
    password = "Totara_2019"
    xpath_username_field = "//*[@id='username']"
    context.browser.find_element_by_xpath(xpath_username_field).send_keys(username)
    xpath_password_field = "//*[@id='password']"
    context.browser.find_element_by_xpath(xpath_password_field).send_keys(password)
    xpath_login_button = "//*[@id='loginbtn']"
    context.browser.find_element_by_xpath(xpath_login_button).submit()
    time.sleep(3)


# user closes lateral menu for view home page in full screen_______________________________________________________________-
@step("click on the button to close and reopen the sidebar")
def step_impl(context):
    btt_xpth = "//a[@id='show-sidebar']/i"
    button = context.browser.find_element_by_xpath(btt_xpth)
    context.browser.execute_script("arguments[0].click();", button)
    time.sleep(1)

    class_name = button.get_attribute('class')
    if class_name == "fas fa-chevron-right":
        context.browser.execute_script("arguments[0].click();", button)
        time.sleep(2)
    else:
        raise NameError('close sidebar action is not executed')


@step("scroll down the right sidebar")
def step_impl(context):
    xpth_target = "//h2[contains(text(),'I miei nuovi badge')]"
    target = context.browser.find_element_by_xpath(xpth_target)
    context.browser.execute_script('arguments[0].scrollIntoView(true);', target)
    time.sleep(2)


@step("scroll down the content of the page")
def step_impl(context):
    xpath_footer = "//footer[@id='page-footer']"
    target_footer = context.browser.find_element_by_xpath(xpath_footer)
    context.browser.execute_script('arguments[0].scrollIntoView(true);', target_footer)
    time.sleep(2)


@then("the sidebar and content of the page should be scrolled")
def step_impl(context):
    expected_result_a = context.browser.find_element_by_xpath("//h2[contains(text(),'I miei nuovi badge')]")
    expected_result_b = context.browser.find_element_by_xpath("//footer[@id='page-footer']")
    if expected_result_a.is_displayed():
        print(expected_result_a)
        if expected_result_b.is_displayed():
            print("both element visible on the screen!")
    else:
        raise NameError('Elements there are not visible on the screen!!!')


# Login.features/Log out......................
@then("navigate to menu dropdown end click esci")
def step_impl(context):
    xpath_user_action_menu = "//*[@class='userbutton']"
    user_menu = context.browser.find_element_by_xpath(xpath_user_action_menu).click()
    time.sleep(0.5)
    xpath_list = "//*[@id='action-menu-0-menu']/li/a"
    options = context.browser.find_elements_by_xpath(xpath_list)
    for i in options:
        if "Esci".upper() in i.text:
            i.click()
        time.sleep(1)
    else:
        raise NameError("Errore!!!")


#topNavigationBar.feature
#-----------Dashboard--------------
@when('user navigates on top navigation bar and click on the "{element}"')
def step_impl(context, element):
    linkText = context.browser.find_element_by_link_text("Dashboard")
    time.sleep(1)
    linkText.click()

@then('Should be back on my dashboard "{my_dashboard}"')
def step_impl(context, my_dashboard):
    xpath_titlePage = "//*[contains(text(), 'et.erickson.it: Expert Teacher')]"
    titlePage = context.browser.find_element_by_xpath(xpath_titlePage).text
    time.sleep(2)
    assert titlePage == my_dashboard
    time.sleep(2)

@when("user clicks on the Expet Teacher logos on the upper left portion")
def step_impl(context):
    xpath_logo = "//*[@class='masthead_logo--header_img img-responsive']"
    logo = context.browser.find_element_by_xpath(xpath_logo).click()
    time.sleep(1)

#
#
# @then('after click on should be returned "SHELL ET" on the new card of browser')
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: Then after click on should be returned "SHELL ET" on the new card of browser')
#
#
# @then('after click on should be returned "Curriculum Formativo: Tutte Le Palestre"')
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: Then after click on should be returned "Curriculum Formativo: Tutte Le Palestre"')
#
#
# @when('user navigates on top navigation bar and click on the item an anvelop "Menu messaggi"')
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(
#         u'STEP: When user navigates on top navigation bar and click on the item an anvelop "Menu messaggi"')
#
#
# @step("clicks again on the item an envelope")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: And clicks again on the item an envelope')
#
#
# @then('"menu messaggi" should be closed')
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: Then "menu messaggi" should be closed')
#
#
# @when('user navigates on top navigation bar and click on the item bell "Notifiche"')
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: When user navigates on top navigation bar and click on the item bell "Notifiche"')
#
#
# @step("clicks again on the item bell")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: And clicks again on the item bell')
#
#
# @when("user navigates on top navigation bar and click on the user's own name")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: When user navigates on top navigation bar and click on the user\'s own name')
#
#
# @step("clicks again on the user's own name")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: And clicks again on the user\'s own name')
#
#
# @then('user\'s menu profile "menu-content" should be closed')
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: Then user\'s menu profile "menu-content" should be closed')