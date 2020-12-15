#xpath: //*[@id="raceContainer"]/div[4]/div[1]/div[1]/div[2]/div[1]/div
#xpath: //*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]/div[1]/div
#xpath: //*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]/div[1]/div
#xpath: //*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]/div[1]/div
#xpath: //*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]/div[1]/div
#xpath: //*[@id="raceContainer"]/div[4]/div[1]/div[1]/div[2]/div[1]/div

import string
import pyautogui
import time
import keyboard
from selenium import webdriver
from bs4 import BeautifulSoup
import random




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




class typer():
    def what():
        htmlsrc = driver.page_source
        htmlpaste = open('html_src.txt', 'w')
        htmlpaste.write(htmlsrc)
        htmlpaste.close()



        htmlreplace = open("html_src.txt", "rt")
        data = htmlreplace.read()
        htmlreplace.close()
        data = data.replace('&nbsp;', ' ')
        htmlreplace = open("html_src.txt", "wt")
        htmlreplace.write(data)
        htmlreplace.close()


        htmlfile = open('html_src.txt', 'r')
        soup = BeautifulSoup(htmlfile, 'lxml')
        htmlfile.close()
        span = soup.find_all('span', class_='dash-letter')
        with open('spans.txt', 'w') as f:
            for spans in span:
                f.write(spans.text)
            f.close()

        spantxt = open('spans.txt', 'r+')
        spantxtdata = spantxt.read()
        spantxt.close()

        spans2txt = open('span2.txt', 'r+')
        for word in spantxtdata:
            listword = list(word)
            for letter in listword:
                spans2txt.write(letter + '\n')
        spans2txt.close()


        def randomdec():
            rando = random.randint(1,30)
            if rando == 1:
                time.sleep(0.1)
            if rando == 2:
                time.sleep(0.2)
            else:
                time.sleep(0)

        def randommistake():
            randlet = random.randint(1,50)
            if randlet == 1:
                string.ascii_letters
                pyautogui.typewrite(random.choice(string.ascii_letters))
                

        writetype = open('span2.txt', 'r+')
        for letter in writetype:
            letter = letter.strip('\n')
            pyautogui.typewrite(letter)
            randomdec()
            randommistake()
        writetype.truncate(0)
        writetype.close()

    while True:
        try:
            q = driver.find_element_by_xpath('//*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]/div[2]')
            if q:
                print ("finding xpath")
                q.click()
                print ("got here")
                #time.sleep(3)
                what()
            else:
                pass
        except:
            pass

        try:
            driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[1]/button').click()
        except:
            pass

        try:
            q = driver.find_element_by_xpath('//*[@id="raceContainer"]/div[1]/div[2]/div[3]/div/div[2]/button')
            if q:
                q.click()
        except:
            pass


        try:
            q = driver.find_elements_by_xpath('//*[@id="raceContainer"]/div[1]/div[1]/div/div/div/div[2]/button')
            if q:
                q.click()
        except:
            pass

        try:
            q = driver.find_elements_by_xpath('//*[@id="root"]/div[1]/div[1]/div[3]/div/div/button')
            if q:
                q.click()
                time.sleep(1)
                driver.find_elements_by_xpath('//*[@id="root"]/div[1]/div[2]/div[3]/div/div[1]/button').click()
        except:
            pass
        try:
            q = driver.find_elements_by_xpath('//*[@id="root"]/div[1]/div[1]/div[3]/div/div[2]/button')
            if q:
                q.click()
                time.sleep(1)
                driver.find_elements_by_xpath('//*[@id="root"]/div[1]/div[2]/div[3]/div/div[1]/button').click()
        except:
            pass
        
        print ("got here end")
