import time
import names  # (names.get_firstname)
from behave import *
from time import sleep
from yaml import load
import random
import sqlite3
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


# function random list
def random_name(list):
    return random.choice(list)


# ______________________Global value___________________________
global_name = ""
global_lastname = ""
global_email = ""


# function wait
def wait_for_xpath_element(context, time_sec, xpath_element):
    time.sleep(0.5)
    i = 0
    status = False
    while i <= time_sec and status != True:
        try:
            context.browser.find_element_by_xpath(xpath_element)
            status = True
        except:
            pass
        time.sleep(1)
        i += 1


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


@then('User should be had the page log-in in "{expected_result}" language')
def step_impl(context, expected_result):
    xpath_language_page = "//option[@value='en']"
    actual_result = context.browser.find_element_by_xpath(xpath_language_page).text
    time.sleep(2)
    if actual_result == 0:
        assert print(expected_result)


# /login in one step with agreement privacy
@given('set up url address "{text}" and execute login with credentials "{username}" and "{password}" and consent site policy')
def step_impl(context, text, username, password):
    context.settings = load(open('features\conf.yaml').read())
    url = context.settings['base_url']
    basic_url = 'https://{}/'.format(url)
    if 'staging' in url or 'dev' in url:
        context.browser.get(basic_url)
    context.browser.get('https://{}/'.format(url) + text)
    time.sleep(0.5)
    xpath_username_field = "//*[@id='username']"
    context.browser.find_element_by_xpath(xpath_username_field).send_keys(username)
    xpath_password_field = "//*[@id='password']"
    context.browser.find_element_by_xpath(xpath_password_field).send_keys(password)
    xpath_login_button = "//*[@id='loginbtn']"
    context.browser.find_element_by_xpath(xpath_login_button).submit()
    time.sleep(1)
    #__Agreement privacy______________________
    try:
        xpath_text_privacy_declaration = "//*[contains(text(), 'Consenso')]"
        declaration_text = context.browser.find_element_by_xpath(xpath_text_privacy_declaration)
        context.browser.execute_script('arguments[0].scrollIntoView(true);', declaration_text)
        xpath_agreement = "//div[@class='tf_element_input']/div/input"
        agreement = context.browser.find_element_by_xpath(xpath_agreement)
        if agreement.get_attribute("id") == "tfiid_option2_tool_sitepolicy_form_userconsentform___rd_0":
            agreement.click()
        else:
            print("Radio button is not found")
        xpath_bttn_send = "//div/input[@id='tfiid_submitbutton_tool_sitepolicy_form_userconsentform']"
        wait_for_xpath_element(context, 0.5, xpath_bttn_send)
        send_bttn = context.browser.find_element_by_xpath(xpath_bttn_send).click()
    except:
        pass

# user closes lateral menu for view home page in full screen_______________________________________________________________-
@step("user clicks on the button on the right corner of the sidebar to close and reopen it")
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


# topNavigationBar.feature
# -----------Dashboard--------------
@when('user navigates on top navigation bar and click on the Dashboard')
def step_impl(context):
    linkText = context.browser.find_element_by_link_text("Dashboard")
    linkText.click()
    time.sleep(2)


# -------------Logo on homePage----------------------
@when("user clicks on the Expert Teacher logos on the upper left part")
def step_impl(context):
    xpath_logo = "//*[@class='masthead_logo--header_img img-responsive']"
    wait_for_xpath_element(context, 3, xpath_logo)
    logo = context.browser.find_element_by_xpath(xpath_logo).click()


@then('should be back on the page of my Dashboard "{element}"')
def step_impl(context, element):
    title = context.browser.title
    assert element == title


# ------------TAB Media Library-------------------------
@when('user navigates on top navigation bar and clicks on the "Media Library"')
def step_impl(context):
    xpath_nav = "//ul/li[3]/a[@class='totaraNav_prim--list_item_link']"
    wait_for_xpath_element(context, 5, xpath_nav)
    nav_list = context.browser.find_element_by_xpath(xpath_nav)
    # open TAB in new windows
    nav_list.send_keys(Keys.CONTROL + Keys.ENTER)
    # focus on the new TAB that is opened
    context.browser.switch_to_window(context.browser.window_handles[1])
    time.sleep(2)
    # came back on the main page
    # context.browser.switch_to_window(context.browser.window_handles[0])
    # time.sleep(2)


@then('should be return the title of the page "{element}"')
def step_impl(context, element):
    title = context.browser.title
    assert element == title
    time.sleep(1)


# --------------------CURRICULUM FORMATIVO----------------------------------
@when('user navigates on the top navigation bar and clicks on the "Curriculum Formativo"')
def step_impl(context):
    xpath_curriculum = "//ul/li[4]/a[@class='totaraNav_prim--list_item_link']"
    wait_for_xpath_element(context, 2, xpath_curriculum)
    curriculum = context.browser.find_element_by_xpath(xpath_curriculum)
    curriculum.click()
    time.sleep(2)


# ------------------MESSAGGE------------------------------------------------
@when('user clicks on "an envelope item" that open and close "Menu messaggi"')
def step_impl(context):
    xpath_message = "//*[@id='nav-message-popover-container']/div[@role='button']"
    wait_for_xpath_element(context, 2, xpath_message)
    menu_message = context.browser.find_element_by_xpath(xpath_message)
    menu_message.click()
    time.sleep(2)
    getText = menu_message.get_attribute('aria-label')
    if getText == "Nascondi finestra dei messaggi":
        context.browser.execute_script("arguments[0].click();", menu_message)
        time.sleep(3)
    else:
        print("Menu message left open!")


@then("message menu should be closed")
def step_impl(context):
    xpath_menu_expanded = "//*[@class='popover-region-container']"
    wait_for_xpath_element(context, 1, xpath_menu_expanded)
    menu_expanded = context.browser.find_element_by_xpath(xpath_menu_expanded)
    check_menu_expanded = menu_expanded.get_attribute('aria-expanded')
    assert check_menu_expanded == "false"


# ------------------NOTIFICHE------------------------------------------------
@when('user navigates on top navigation bar click on the bell item that open and close notification menu')
def step_impl(context):
    xpath_notification = "//*[@class='totaraNav_prim--side']/div[4]/div"
    wait_for_xpath_element(context, 1, xpath_notification)
    notification_menu = context.browser.find_element_by_xpath(xpath_notification)
    notification_menu.click()
    time.sleep(2)
    getText = notification_menu.get_attribute('aria-label')
    if getText == "Nascondi finestra delle notifiche":
        context.browser.execute_script("arguments[0].click();", notification_menu)
        time.sleep(3)
    else:
        print("Menu message left open!")


@then('"menu notifiche" should be closed')
def step_impl(context):
    xpath_menu_expanded = "//*[@class='totaraNav_prim--side']/div[4]/div[2]"
    wait_for_xpath_element(context, 1, xpath_menu_expanded)
    menu_expanded = context.browser.find_element_by_xpath(xpath_menu_expanded)
    check_menu_expanded = menu_expanded.get_attribute('aria-expanded')
    assert check_menu_expanded == "false"


# ------------------User MENU------------------------------------------------
@when("user navigates on top navigation bar click on the user text name that open user's menu")
def step_impl(context):
    xpath_user_action_menu = "//*[@id='action-menu-0']/ul/li/a/span[@class='userbutton']"
    user_menu = context.browser.find_element_by_xpath(xpath_user_action_menu)
    user_menu.click()
    time.sleep(0.5)


@then('"user\'s menu" should open')
def step_impl(context):
    xpath_usermenu_open = "//*[@class='usermenu']/div"
    wait_for_xpath_element(context, 2, xpath_usermenu_open)
    users_menu = context.browser.find_element_by_xpath(xpath_usermenu_open)
    time.sleep(1)
    get_text = users_menu.get_attribute('class')
    assert get_text == "moodle-actionmenu nowrap-items show"


# user profile within the left sidebar------------------------------------------------------------------
@step("click on user's image profile on the left side bar")
def step_impl(context):
    xpath_users_image = "//*[@class='myprofileitem picture']/a"
    wait_for_xpath_element(context, 1, xpath_users_image)
    users_image = context.browser.find_element_by_xpath(xpath_users_image)
    users_image.click()
    time.sleep(2)
    # raise NotImplementedError(u'STEP: When user navigates to the right side bar')


@step('within the section "Dettagli dell\'utente" click on "modifica"')
def step_impl(context):
    xpath_btn_modified = "//*[@class='editprofile']/span/a"
    wait_for_xpath_element(context, 2, xpath_btn_modified)
    btn_modified = context.browser.find_element_by_xpath(xpath_btn_modified).click()
    time.sleep(3)

@when('click on the link "Annulla cambio email" and insert user\'s firstname, last name, email"')
def step_impl(context):
    try:
        xpath = "//*[@id='fitem_id_emailpending']/div[@class='felement fstatic']/a"
        wait_for_xpath_element(context, 1, xpath)
        cancell_change_email = context.browser.find_element_by_xpath(xpath)
        cancell_change_email.click()
    except:
        pass
    time.sleep(2)
    list = [['Andry', 'Sergio', 'Igor'], ['Hamilton', 'Clarknet', 'Wenture'],
            ['andry@nomil.invalid', 'sergio@nomail.invalid', 'igor@nomail.invalid']]
    xpath_name = "//*[@class='fitem required fitem_ftext  ']/div[2]/input"
    wait_for_xpath_element(context, 2, xpath_name)
    name = context.browser.find_elements_by_xpath(xpath_name)
    for key in name:

        if key.get_attribute('id') == "id_firstname":
            key.clear()
            insert_name = random_name(list[0])
            global global_name
            global_name = insert_name
            key.send_keys(global_name)
        elif key.get_attribute('id') == "id_lastname":
            key.clear()
            insert_lastname = random_name(list[1])
            global global_lastname
            global_lastname = insert_lastname
            key.send_keys(global_lastname)
        elif key.get_attribute('id') == "id_email":
            key.clear()
            insert_email = random_name(list[2])
            global global_email
            global_email = insert_email
            key.send_keys(global_email)
        else:
            print("error")

@step('click on "Aggiornamento profilo" and carry out modification clicking on "Continua"')
def step_impl(context):
    context.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # scroll down page
    xpath_update = "//*[@class='felement fgroup']/input[1]"
    wait_for_xpath_element(context, 0.5, xpath_update)
    update_userprofile = context.browser.find_element_by_xpath(xpath_update).click()
    try:
        xpath_btn_continua = "//*[@class='form-submit btn-primary']"  # button continua after approved change email adress
        wait_for_xpath_element(context, 1, xpath_btn_continua)
        btn_continua = context.browser.find_element_by_xpath(xpath_btn_continua)
        if btn_continua.get_attribute('value') == "Continua":
            btn_continua.click()
        else:
            print("is not visible on the page")
    except:
        pass

@then("user's firstname, surname and email should be changed")
def step_impl(context):
    expected_result = global_name + " " + global_lastname
    print(expected_result)
    xpath_fullname = "//*[@class='breadcrumb-nav']//li[3]/span/a/span"
    wait_for_xpath_element(context, 1, xpath_fullname)
    fullname = context.browser.find_element_by_xpath(xpath_fullname).text
    print(fullname)
    assert expected_result == fullname

# Scenario: user deny agreement policy from through user's profile
@step('scroll down the page and focus on the section "Administration" and click on the link "Site policy consents"')
def step_impl(context):
    # xpath_target = "//*[@class='block col-md-12']/h3[contains(text(), 'Amministrazione')]"
    xpath_target = "//ul[@class='mtul']/li[2]/span/a"
    target = context.browser.find_element_by_xpath(xpath_target)
    context.browser.execute_script('arguments[0].scrollIntoView(true);', target)

@step('click on the names of the policies and select "Nego il consenso"')
def step_impl(context):
