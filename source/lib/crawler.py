import random
import requests
from uuid import uuid4

from .url import Url
from .page_scraper import PageScraper

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

    def crawled_count(self):
        return len([url for url in self._url_list if url.crawled])

    def add_url_as_string(self, url_string):
        url_obj = Url(url_string)
        self._url_list.append(url_obj)

    def _get_next_uncrawled_url(self):
        for url_obj in self._url_list:
            if url_obj.crawled is False and url_obj.status_code != 404:
                return url_obj

    def _crawl_url(self, url_obj):
        r = requests.get(url_obj.url)
        if r.status_code == 404:
            url_obj.status_code = 404
            return # url_obj.crawled remains False
        page_scraper = PageScraper(r.text)
        links = page_scraper.links
        for link in links:
            new_url_obj = Url(link, referrer=url_obj.url)
            if new_url_obj.belongs_to_domain(self.domain):
                self._url_list.append(new_url_obj)
        url_obj.crawled = True

    def crawl(self):
        while True:
            next = self._get_next_uncrawled_url()
            if next is not None:
                self._crawl_url(next)
            else:
                break
