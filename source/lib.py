import random
from uuid import uuid4

class Crawler(object):

    def __init__(self, start_url):
        self._url_list = []
        self.add_url_as_string(start_url)

    @property
    def url_list_as_strings(self):
        return tuple(url_object.url for url_object in self._url_list)

    def add_url_as_string(self, url_string):
        url_obj = Url(url_string)
        self._url_list.append(url_obj)

    def _get_next_uncrawled_url(self):
        for url_obj in self._url_list:
            if url_obj.crawled is False:
                return url_obj

    def _get_random_bool(self):
        return bool(random.getrandbits(1))

    def _crawl_url(self, url_obj):
        if self._get_random_bool():
            self.add_url_as_string('dummy-url-{}'.format(uuid4()))
        url_obj.crawled = True

    def crawl(self):
        while True:
            next = self._get_next_uncrawled_url()
            if next is not None:
                self._crawl_url(next)
            else:
                break


class Url(object):

    def __init__(self, url_string):
        self._url = url_string
        self.crawled = False

    def __str__(self):
        return '<Url object - _url: {} - crawled: {}>'.format(self._url, self.crawled)

    @property
    def url(self):
        return self._url
