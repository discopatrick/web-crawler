class Url(object):

    def __init__(self, url_string):
        self._url = url_string
        self.crawled = False

    def __str__(self):
        return '<Url object - _url: {} - crawled: {}>'.format(self._url, self.crawled)

    @property
    def url(self):
        return self._url
