class Crawler(object):

    def __init__(self):
        self._url_list = []

    @property
    def url_list(self):
        return tuple(url_object.url for url_object in self._url_list)

    def add_url(self, url):
        url_obj = Url(url)
        self._url_list.append(url_obj)

class Url(object):

    def __init__(self, url):
        self._url = url

    @property
    def url(self):
        return self._url
