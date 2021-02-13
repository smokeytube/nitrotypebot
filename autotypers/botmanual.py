import string
import pyautogui
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import random
import keyboard
import lxml


class botmanual:
    def botmanualmain(chromedriverdir):
        perfectint = input("No mistakes (warning: could trigger anticheat if used long enough) (y/n): ")

        driver = webdriver.Chrome(chromedriverdir)
        driver.implicitly_wait(5)
        driver.get('https://www.nitrotype.com/login')

        if perfectint == "n" or perfectint == "no":
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

                spantxt = open('textfiles/spans.txt', 'r+')
                spantxtdata = spantxt.read()
                spantxt.close()

                spans2txt = open('textfiles/span2.txt', 'r+')
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
                        

                writetype = open('textfiles/span2.txt', 'r+')
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

        if perfectint == "y" or perfectint == "yes":
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

                spantxt = open('textfiles/spans.txt', 'r+')
                spantxtdata = spantxt.read()
                spantxt.close()

                spans2txt = open('textfiles/span2.txt', 'r+')
                for word in spantxtdata:
                    listword = list(word)
                    for letter in listword:
                        spans2txt.write(letter + '\n')
                spans2txt.close()
                writetype = open('textfiles/span2.txt', 'r+')
                for letter in writetype:
                    letter = letter.strip('\n')
                    pyautogui.typewrite(letter)
                writetype.truncate(0)
                writetype.close()

                    
            while True:
                if keyboard.is_pressed('`') or keyboard.is_pressed('~'):
                    what()