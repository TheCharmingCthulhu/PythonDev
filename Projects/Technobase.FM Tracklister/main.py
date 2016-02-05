import rest

class TBBase(object):
    def __init__(self):
        self.scheme = "https://"
        self.baseurl = "www.technobase.fm"
        self.rest = rest.REST(self.scheme, self.baseurl)

    def get_url(self):
        return self.rest.static_base_url


class TBTracklist(TBBase):
    def __init__(self):
        super(TBTracklist, self).__init__()
        self.url = super(TBTracklist, self).get_url()

    def get_playlist(self):
        self.rest.get_element('//*[@id="MainContent"]/div[2]/div[3]/div')


if __name__ == "__main__":
    tbanalyzer = TBTracklist()
    tbanalyzer.get_playlist()
