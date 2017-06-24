class Crawler(object):

    def add_url(self, url):
        pass

class Url(object):

    def __init__(self, url):
        self._url = url

    @property
    def url(self):
        return self._url
