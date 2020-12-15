#xpath: //*[@id="raceContainer"]/div[4]/div[1]/div[1]/div[2]/div[1]/div
#xpath: //*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]/div[1]/div
#xpath: //*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]/div[1]/div
#xpath: //*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]/div[1]/div
#xpath: //*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]/div[1]/div
#xpath: //*[@id="raceContainer"]/div[4]/div[1]/div[1]/div[2]/div[1]/div

import pyautogui
import time
import keyboard
from selenium import webdriver
from  html.parser import HTMLParser
from bs4 import BeautifulSoup




chromedriverdir = 'chromedriver86.exe'
# chromedriverdir = 'C:\webdrivers\chromedriver.exe'
driver = webdriver.Chrome(chromedriverdir)
driver.implicitly_wait(5)
driver.get('https://www.nitrotype.com/login')

driver.find_element_by_xpath('//*[@id="username"]').send_keys('Doctorwail')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('PASSWORD')
driver.find_element_by_xpath('//*[@id="root"]/div/div/main/div/section/div[2]/div/div[3]/form/button').click()

driver.find_element_by_xpath('//*[@id="root"]/div/header/div/div[3]/div[1]/a').click()

x = 0

while x != 1:
    try:
        driver.find_element_by_xpath('//*[@id="raceContainer"]/div[4]/div[1]/div[1]/div[2]/div[1]/div')
        x = x+1
    except:
        pass

    try:
        driver.find_element_by_xpath('//*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]/div[1]/div')
        x = x+1
    except:
        pass




htmlsrc = driver.page_source
htmlpaste = open('html_src.txt', 'w')
htmlpaste.write(htmlsrc)
htmlpaste.close()



htmlreplace = open("html_src.txt", "rt")
data = htmlreplace.read()
data = data.replace('&nbsp;', ' ')
htmlreplace.close()
htmlreplace = open("html_src.txt", "wt")
htmlreplace.write(data)
htmlreplace.close()


htmlfile = open('html_src.txt', 'r')
soup = BeautifulSoup(htmlfile, 'lxml')
span = soup.find_all('span', class_='dash-letter')
with open('spans.txt', 'w') as f:
    for spans in span:
        f.write(spans.text)
    f.close()


spansreplace = open("spans.txt", "rt")
data = spansreplace.read()
data = data.replace('&nbsp;', ' \n')
spansreplace.close()
spansreplace = open("spans.txt", "wt")
spansreplace.write(data)
spansreplace.close()

x = 1
while x != 2:
    if keyboard.is_pressed('q'):
        try:
            driver.find_element_by_xpath('//*[@id="raceContainer"]/div[4]/div[1]/div[1]/div[2]/div[1]/div').click()
            x = x+1
        except:
            pass

        try:
            driver.find_element_by_xpath('//*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]/div[1]/div').click()
            x = x+1
        except:
            pass
        writetype = open('spans.txt', 'r')
        for word in writetype:
            pyautogui.typewrite(word)
    else:
        pass