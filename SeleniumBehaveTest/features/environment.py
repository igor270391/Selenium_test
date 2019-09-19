from yaml import load
from selenium import webdriver
import os, time
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