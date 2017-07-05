import requests
import time
import random
from queue import Queue
from threading import Thread

from .url import Url
from .page_scraper import PageScraper


class Crawler(object):

    # TODO: add ignore_query argument
    def __init__(self, start_url, ignore_fragment=False):
        self._queue = Queue()
        self._url_list = []
        self._ignore_fragment = ignore_fragment
        start_url_obj = self.urlobj_factory(start_url)
        self._start_url = start_url_obj

        # TODO: DRY appending to list/queue
        self._url_list.append(start_url_obj)
        self._queue.put(start_url_obj)

        self._num_threads = 5

    @property
    def url_list_as_strings(self):
        return tuple(url_object.url for url_object in self._url_list)

    @property
    def domain(self):
        return self._start_url.domain

    def urlobj_factory(self, url_string, referrer=None):
        url_obj = Url(url_string, trim_fragment=self._ignore_fragment,
                      referrer=referrer)
        return url_obj

    def crawled_count(self):
        return len([url for url in self._url_list if url.crawled])

    def _already_in_list(self, new_url_obj):
        for url_obj in self._url_list:
            if url_obj.url == new_url_obj.url:
                return True
        return False

    def _crawl_url(self, url_obj):
        # wait between 1 and 3 seconds before requesting url
        time.sleep(random.uniform(1.0, 3.0))
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
            new_url_obj = self.urlobj_factory(link, referrer=url_obj.url)
            if new_url_obj.belongs_to_domain(self.domain) \
                    and not self._already_in_list(new_url_obj):
                print('adding {} to the list and queue'.format(
                    new_url_obj.url))

                # TODO: DRY appending to list/queue
                self._url_list.append(new_url_obj)
                self._queue.put(new_url_obj)

        url_obj.crawled = True

    def _get_report(self):
        report = ""
        for url_obj in self._url_list:
            if url_obj.crawled:
                report += ('[page] ' + url_obj.url + '\n')
        report += '{} link(s) crawled'.format(self.crawled_count()) + '\n'
        return report

    def _crawl_thread(self):
        while True:
            next = self._queue.get()
            self._crawl_url(next)
            self._queue.task_done()

    def crawl(self):
        for i in range(self._num_threads):
            worker = Thread(target=self._crawl_thread)
            worker.setDaemon(True)
            worker.start()
        self._queue.join()
        return self._get_report()
