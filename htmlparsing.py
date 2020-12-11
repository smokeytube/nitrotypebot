from  html.parser import HTMLParser

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
    f = open("html.html")
    if f.mode == 'r':
        contents: str = f.read()
        parser.feed(contents)


if __name__ == "__main__":
    main()