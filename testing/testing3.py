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


class typer():
    def what():
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
            rando = random.randint(1,12)
            if rando == 1:
                time.sleep(0.1)
            if rando == 2:
                time.sleep(0.2)
            else:
                time.sleep(0)

        def randommistake():
            randlet = random.randint(1,30)
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
        if keyboard.is_pressed('`'):
            what()            

