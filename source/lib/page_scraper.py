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

    def _get_assets_from_html(self):
        # TODO: refactor
        return [
            'style.css',
            'script.js',
            'this-page.html',
            'smiley-face.jpg',
        ]

    @property
    def links(self):
        return self._get_links_from_html()

    @property
    def assets(self):
        return self._get_assets_from_html()
