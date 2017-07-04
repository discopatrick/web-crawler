import requests
import threading
import time

from .url import Url
from .page_scraper import PageScraper


class Crawler(object):

    # TODO: add ignore_query argument
    def __init__(self, start_url, ignore_fragment=False):
        self._url_list = []
        self._ignore_fragment = ignore_fragment
        # TODO: DRY Url object creation
        start_url_obj = Url(start_url, trim_fragment=self._ignore_fragment)
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

    def _get_next_uncrawled_url(self):
        for url_obj in self._url_list:
            if url_obj.crawled is False \
                    and url_obj.status_code != 404 \
                    and url_obj.is_html:
                return url_obj

    def _already_in_list(self, new_url_obj):
        for url_obj in self._url_list:
            if url_obj.url == new_url_obj.url:
                return True
        return False

    def _crawl_url(self, url_obj):
        print('Thread {} crawling {}'.format(
            threading.currentThread().getName(),
            url_obj.url))
        r = requests.get(url_obj.url)
        if r.status_code == 404:
            url_obj.status_code = 404
            return  # url_obj.crawled remains False
        elif not r.headers['content-type'].startswith('text/html'):
            url_obj.is_html = False
            return

        page_scraper = PageScraper(r.text)
        links = page_scraper.links

        # TODO: make inventory of all page assets for report

        for link in links:
            # TODO: DRY Url object creation
            new_url_obj = Url(link, trim_fragment=self._ignore_fragment,
                              referrer=url_obj.url)
            if new_url_obj.belongs_to_domain(self.domain) \
                    and not self._already_in_list(new_url_obj):
                self._url_list.append(new_url_obj)

        url_obj.crawled = True

    def _get_report(self):
        report = ""
        for url_obj in self._url_list:
            if url_obj.crawled:
                report += ('[page] ' + url_obj.url + '\n')
        report += '{} link(s) crawled'.format(self.crawled_count()) + '\n'
        return report

    def crawl(self):
        while True:
            time.sleep(0.25)
            next = self._get_next_uncrawled_url()
            if next is not None:
                t = threading.Thread(target=self._crawl_url,
                                     args=(next,))
                t.start()
            else:
                break
        return self._get_report()
