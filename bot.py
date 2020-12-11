#xpath: //*[@id="raceContainer"]/div[4]/div[1]/div[1]/div[2]/div[1]/div
#xpath: //*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]/div[1]/div
#xpath: //*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]/div[1]/div
#xpath: //*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]/div[1]/div
#xpath: //*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]/div[1]/div
#xpath: //*[@id="raceContainer"]/div[4]/div[1]/div[1]/div[2]/div[1]/div

import pyautogui
import time
from selenium import webdriver
from  html.parser import HTMLParser




chromedriverdir = 'chromedriver86.exe'
# chromedriverdir = 'C:\webdrivers\chromedriver.exe'
driver = webdriver.Chrome(chromedriverdir)
driver.implicitly_wait(5)
driver.get('https://www.nitrotype.com/login')

driver.find_element_by_xpath('//*[@id="username"]').send_keys('USERNAME')
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

metacount = 0

class MyHTMLParser(HTMLParser):
    print('')

    def handle_comment(self, data):
        print("comment", data)
        pos = self.getpos()
        print("At line: ", pos[0], data, pos[1])

    def handle_starttag(self, tag, attrs):
        global metacount
        if tag == 'meta':
            metacount += 1
        print("tag:", tag)
        pos = self.getpos()
        print("at line", pos[0], " position ", pos[1])

    def handle_data(self, data):
        if (data.isspace()):
            return
        print("data", data)
        pos = self.getpos()
        print("At line: ", pos[0], data, pos[1])

def main():
    parser = MyHTMLParser()
    f = open("samplehtml.html")
    if f.mode == 'r':
        contents: str = f.read()
        parser.feed(contents)


if __name__ == "__main__":
    main()