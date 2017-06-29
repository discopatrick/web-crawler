from urllib.parse import urlparse, urljoin

class Url(object):

    def __init__(self, url_string, referrer=None):
        self._url = url_string
        self.crawled = False
        self._referrer = referrer

    def __str__(self):
        return '<Url object - _url: {} - crawled: {}>'.format(self._url, self.crawled)

    @property
    def url(self):
        return urljoin(self._referrer, self._url)

    @property
    def domain(self):
        return self._get_domain()

    def _get_domain(self):
        return urlparse(self._url).netloc

    def belongs_to_domain(self, domain):
        parsed = urlparse(self.url)
        return domain == parsed.netloc
