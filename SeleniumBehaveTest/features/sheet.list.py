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