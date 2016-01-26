import requests

class TBBase(object):

    def __init__(self):
        self.scheme = "https://"
        self.baseurl = "www.technobase.fm"

    def get_url(self):
        return "{0}{1}".format(self.scheme, self.baseurl)

class TBTracklist(TBBase):

    def __init__(self):
        super(TBTracklist, self).__init__()
        self.url = ""
        self.request = ""

    def get_playlist(self):
        self.url = "{0}{1}".format(super(TBTracklist, self).get_url(), "/tracklist/")
        self.request = requests.get(self.url)



if __name__ == "__main__":
    tbanalyzer = TBTracklist()
    tbanalyzer.get_playlist()
