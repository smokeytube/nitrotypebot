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
from bs4 import BeautifulSoup
import random








class typer():
    def what():
        htmlpaste = open('html_src.txt', 'w')
        htmlpaste.write('bruh')
        htmlpaste.close()



        htmlreplace = open("html_src.txt", "rt")
        data = htmlreplace.read()
        data = data.replace('&nbsp;', ' ')
        htmlreplace.close()
        htmlreplace = open("html_src.txt", "wt")
        htmlreplace.write(data)
        htmlreplace.close()


        span = ('hello bababab ba hi dababy')
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
            if 2 == 2:
                #time.sleep(3)
                what()
            else:
                pass
        except:
            pass

        try:
            print ("bruh")
        except:
            print ("what")

        try:
            if 2 == 2:
                print ('correct')
        except:
            pass

        try:
            if 3 == 2:
                print ("how")
        except:
            pass
        time.sleep(1)