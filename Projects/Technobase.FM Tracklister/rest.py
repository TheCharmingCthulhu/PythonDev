import requests, html_fusion

class REST(object):
    def __init__(self, scheme, base_url):
        self.static_base_url = scheme + base_url
        self.base_url = scheme + base_url
        self.path_seperator = '\\'

    def get_link(self):
        return self.base_url

    def next_link(self, link):
        self.base_url = self.base_url + "\\" + link

    def prev_link(self):
        index, pos = 0, 0
        while True:
            index = self.base_url.find(self.path_seperator, index + 1)
            if index == -1:
                break
            else:
                pos = index
        self.base_url = self.base_url[:pos]
        return self.base_url

    def root_link(self):
        while True:
            self.base_url = self.prev_link()
            if self.base_url.find("\\") == -1:
                break

    def set_link(self, link):
        self.base_url = self.static_base_url + "\\" + self.base_url

    def get_element(self, xpath):
        r = requests.get(self.base_url)
