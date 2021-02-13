import os
from discord_webhook import DiscordWebhook

from autotypers.bot import bot as bot
from autotypers.botguest import botguest as botguest
from autotypers.botguestinstant import botguestinstant as botguestinstant
from autotypers.botguestmanual import botguestmanual as botguestmanual
from autotypers.botmanual import botmanual as botmanual

print ("""
 _______  .__  __                 __                          __________        __   
 \      \ |__|/  |________  _____/  |_ ___.__.______   ____   \______   \ _____/  |_ 
 /   |   \|  \   __\_  __ \/  _ \   __<   |  |\____ \_/ __ \   |    |  _//  _ \   __|
/    |    \  ||  |  |  | \(  <_> )  |  \___  ||  |_> >  ___/   |    |   (  <_> )  |  
\____|__  /__||__|  |__|   \____/|__|  / ____||   __/ \___  >  |______  /\____/|__|  
        \/                             \/     |__|        \/          \/            
""")


chrmdirvs = int(input("Integer what chrome version to use? (Go to chrome://version/ in chrome and find your version): "))
chromedriverdir = f'webdrivers/chromedriver{chrmdirvs}.exe'

print ("1} Type on your account (~100 wpm)")
print ('\n')
print ("2} Type as guest (~100 wpm)")
print ("3} Instant type as guest! (4,000-10,000 wpm)")
print ('\n')
print ("Press '`' or '~' for the manual start")
print ("4} Manual start on account (80-110wpm)")
print ("5} Manual start on guest (6,000-12,000wpm)")
print ('\n')
print ("6} How to use this program (youtube video)")
print ('\n')

while True:
    inum = int(input("Select an option: "))
    if inum >= 7:
        print ('Not a valid option.')
    else:
        break


try:
    if inum == 1:
        bot.botmain(chromedriverdir)

    elif inum == 2:
        botguest.botguestmain(chromedriverdir)

    elif inum == 3:
        botguestinstant.botguestinstantmain(chromedriverdir)

    elif inum == 4:
        botguestmanual.botguestmanualmain(chromedriverdir)

    elif inum == 5:
        botmanual.botmanualmain(chromedriverdir)
    
    elif inum == 6:
        os.system('start "" https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    
except Exception as w̷͇̝̥̟̬͓̯̼̻͎̫͍̖͎̗͑͆̽̍̚̕h̴̨̧͍̪̭̦̍̓a̶̡̦͍͙̠͚͇̣̹͕̾́́͑̓͛̿͑̋̎̆͘͜t̶̳͘:
    print(w̷͇̝̥̟̬͓̯̼̻͎̫͍̖͎̗͑͆̽̍̚̕h̴̨̧͍̪̭̦̍̓a̶̡̦͍͙̠͚͇̣̹͕̾́́͑̓͛̿͑̋̎̆͘͜t̶̳͘)
    print('You are not using the right version of chromedriver. Type chrome://version/ ')
    print('into google chrome to find the right version.\n')
    reporttoowner = input('Not the problem? Report the problem to me (y/n):')
    while True:
        if reporttoowner == 'y' or reporttoowner == 'yes':
            print ('Reporting...')
            webhook = DiscordWebhook(url='https://discord.com/api/webhooks/805297441506721812/-IUbHcOFNmkWUjN4j87PooeakkOCrlPNAJSnLpdvTCTkV0euPxnQYvhC-vcfoJqgGRrO', content=f'{w̷͇̝̥̟̬͓̯̼̻͎̫͍̖͎̗͑͆̽̍̚̕h̴̨̧͍̪̭̦̍̓a̶̡̦͍͙̠͚͇̣̹͕̾́́͑̓͛̿͑̋̎̆͘͜t̶̳͘}')
            webhook.execute()
            print ('Reported')
            break
        elif reporttoowner == 'n' or reporttoowner == 'no':
            break
        else:
            print('Type yes or no')

