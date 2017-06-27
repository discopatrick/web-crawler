from pyquery import PyQuery as pq

class PageScraper(object):

    def __init__(self, html):
        self._html = html

    def _get_links_from_html(self):
        doc = pq(self._html)
        anchor_elements = doc('a')
        anchor_hrefs = []
        for el in anchor_elements:
            anchor_hrefs.append(pq(el).attr['href'])
        return anchor_hrefs

    @property
    def links(self):
        return self._get_links_from_html()
