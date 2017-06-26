import random
from uuid import uuid4

from .url import Url

class Crawler(object):

    def __init__(self, start_url):
        self._url_list = []
        start_url_obj = Url(start_url)
        self._start_url = start_url_obj
        self._url_list.append(start_url_obj)

    @property
    def url_list_as_strings(self):
        return tuple(url_object.url for url_object in self._url_list)

    @property
    def domain(self):
        return self._start_url.domain

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
