import string
import pyautogui
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import random
import keyboard



class botguestmanual:
    def botguestmanualmain(chromedriverdir):
        driver = webdriver.Chrome(chromedriverdir)
        driver.implicitly_wait(5)
        driver.get('https://www.nitrotype.com/race')

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

                        
        while True:
            if keyboard.is_pressed('`') or keyboard.is_pressed('~'):
                what()