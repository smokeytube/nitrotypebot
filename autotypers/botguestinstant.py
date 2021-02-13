#WARNING: I advise strongly against modifying the code
#to use on your nitrotype account. The anticheat will
#instantly ban you.

import string
import pyautogui
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import random


class botguestinstant:
    def botguestinstantmain(chromedriverdir):
        driver = webdriver.Chrome(chromedriverdir)
        driver.implicitly_wait(5)
        driver.get('https://www.nitrotype.com/race')

        try:
            if driver.find_element_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]'):
                    driver.find_element_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]').click()
        except:
            pass


        driver.find_element_by_xpath('//*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[3]/div/button').click()



        def what():
            htmlsrc = driver.page_source
            htmlpaste = open('textfiles/html_src.txt', 'w')
            htmlpaste.write(htmlsrc)
            htmlpaste.close()



            htmlreplace = open("textfiles/html_src.txt", "rt")
            data = htmlreplace.read()
            htmlreplace.close()
            data = data.replace('&nbsp;', ' ')
            htmlreplace = open("textfiles/html_src.txt", "wt")
            htmlreplace.write(data)
            htmlreplace.close()


            htmlfile = open('textfiles/html_src.txt', 'r')
            soup = BeautifulSoup(htmlfile, 'lxml')
            htmlfile.close()
            span = soup.find_all('span', class_='dash-letter')
            with open('textfiles/spans.txt', 'w') as f:
                for spans in span:
                    f.write(spans.text)
                f.close()

            writetype = open('textfiles/spans.txt', 'r+')
            for letter in writetype:
                letter = letter.strip('\n')
                pyautogui.typewrite(letter)
            writetype.truncate(0)
            writetype.close()

            
        def typing():
            try:
                q = driver.find_element_by_xpath('//*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]/div[2]')
                if q:
                    q.click()
                    what()
                else:
                    pass
            except:
                pass


                            
        while True:
            
            typing()

            try:
                q = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[1]/button')
                if q:
                    q.click()
            except:
                pass


            try:
                q = driver.find_element_by_xpath('//*[@id="raceContainer"]/div[1]/div[2]/div[3]/div/div[2]/button')
                if q:
                    q.click()
                    while True:
                        try:
                            typing()
                            break
                        except:
                            pass

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

            

