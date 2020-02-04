from yaml import load
from selenium import webdriver
import os
def before_scenario(context, scenario):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('window-size=1920x1080')
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--lang=it')
    # # chrome_options.add_argument("--kiosk")
    chrome_options.add_argument('--disable-popup-blocking')
    chrome_options.add_argument("start-maximized")
    context.browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options= chrome_options)

# default base url
def before_all(context):
    context.base_url = os.getenv('BASE_URL', "https://testet.mediatouch.it")



# def after_scenario(context, feature):
#     print("after scenario")
#
#
# def before_step(context, step):
#     print("before step")
#
#
# def before_feature(context, feature):
#     print("before feature")