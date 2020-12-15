spantxt = open('span.txt', 'r+')
spantxtdata = spantxt.read()
spantxt.close()

spans2txt = open('span2.txt', 'r+')
for word in spantxtdata:
    listword = list(word)
    for letter in listword:
        spans2txt.write(letter + '\n')
spans2txt.close()

