from urllib.parse import urlparse, urlunparse, urljoin

class Url(object):

    def __init__(self, url_string, referrer=None, trim_query=False,
      trim_fragment=False):
        self._url = url_string
        self.crawled = False
        self._referrer = referrer
        self.status_code = None
        self.is_html = True
        self._trim_query = trim_query
        self._trim_fragment = trim_fragment

    def __str__(self):
        template = '<Url object - _url: {} - crawled: {}>'
        return template.format(self._url, self.crawled)

    @property
    def url(self):
        fully_qualified_url = urljoin(self._referrer, self._url)

        if not self._trim_query and not self._trim_fragment:
            return fully_qualified_url

        p = urlparse(fully_qualified_url)
        if self._trim_query:
            p = p._replace(query=None)
        if self._trim_fragment:
            p = p._replace(fragment=None)

        return urlunparse(p)


    @property
    def domain(self):
        return self._get_domain()

    def _get_domain(self):
        return urlparse(self._url).netloc

    def belongs_to_domain(self, domain):
        parsed = urlparse(self.url)
        return domain == parsed.netloc
