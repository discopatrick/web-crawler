class Crawler(object):

    def __init__(self):
        self._url_list = []

    @property
    def url_list(self):
        return tuple(self._url_list)

    def add_url(self, url):
        self._url_list.append(url)

class Url(object):

    def __init__(self, url):
        self._url = url

    @property
    def url(self):
        return self._url
