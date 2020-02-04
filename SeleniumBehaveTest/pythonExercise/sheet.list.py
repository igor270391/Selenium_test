# import mysql.connector as mys

"""
#explicit/implicit time____________
# # WebDriverWait(context, 10).until(EC.presence_of_element_located((By.ID, "xxx")))

    # wait = WebDriverWait(context, 10, poll_frequency=1,
    #                      ignored_exceptions=[NoSuchElementException,
    #                                          ElementNotSelectableException,
    #                                          StaleElementReferenceException,
    #                                          ElementNotVisibleException])
    # element = wait.until(EC.element_located_to_be_selected(By.XPATH, "xxxx"))
    # element.click()
"""
# reload/refresh page___________
# context.browser.execute_script("location.reload()")
#         time.sleep(2)

# #assert
# title = context.browser.title
#     assert element == title


# для url_________
# @given('url address "{text}"')
# # def step_impl(context, text):
# #     context.settings = load(open('features\conf.yaml').read())
# #     url = context.settings['base_url']
# #     basic_url = 'https://{}/'.format(url)
# #     if 'staging' in url or 'dev' in url:
# #         context.browser.get(basic_url)
# #     context.browser.get('https://{}/'.format(url) + text)
# #     time.sleep(2)


