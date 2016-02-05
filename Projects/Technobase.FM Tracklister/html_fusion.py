import htmllib

class HTMLFusion(htmllib.HTMLParser):
    def __init__(self, content):
        self.content = content


x = HTMLFusion("test")