from bs4 import BeautifulSoup


htmlreplace = open("html.txt", "rt")
data = htmlreplace.read()
data = data.replace('&nbsp;', ' ')
htmlreplace.close()
htmlreplace = open("html.txt", "wt")
htmlreplace.write(data)
htmlreplace.close()


htmlfile = open('html.txt', 'r')
soup = BeautifulSoup(htmlfile, 'lxml')
span = soup.find_all('span', class_='dash-letter')
with open('spans.txt', 'w') as f:
    for spans in span:
        f.write(spans.text)







#&nbsp;

# spans = open("spans.txt", "rt")
# data = spans.read()
# data = data.replace('�', 'tooooo')
# spans.close()
# spans = open("spans.txt", "wt")
# spans.write(data)
# spans.close()