#xpath: //*[@id="raceContainer"]/div[4]/div[1]/div[1]/div[2]/div[1]/div
#xpath: //*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]/div[1]/div
#xpath: //*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]/div[1]/div
#xpath: //*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]/div[1]/div
#xpath: //*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]/div[1]/div
#xpath: //*[@id="raceContainer"]/div[4]/div[1]/div[1]/div[2]/div[1]/div



# import string
# import pyautogui
import time
# import keyboard
from selenium import webdriver
# from bs4 import BeautifulSoup
# import random
# import msvcrt
from typer import *




chromedriverdir = 'chromedriver86.exe'
driver = webdriver.Chrome(chromedriverdir)
driver.implicitly_wait(5)
driver.get('https://www.nitrotype.com/race')

try:
    if driver.find_element_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]'):
            driver.find_element_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]').click()
except:
    pass


driver.find_element_by_xpath('//*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[3]/div/button').click()

time.sleep(5)


typer()            

