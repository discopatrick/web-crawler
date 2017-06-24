class Crawler(object):

    def __init__(self):
        self._url_list = []

    @property
    def url_list(self):
        list_of_urls = [url_object.url for url_object in self._url_list]
        return tuple(list_of_urls)

    def add_url(self, url):
        url_obj = Url(url)
        self._url_list.append(Url)

class Url(object):

    def __init__(self, url):
        self._url = url

    @property
    def url(self):
        return self._url
