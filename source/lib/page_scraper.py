from pyquery import PyQuery as pq

class PageScraper(object):

    def __init__(self, html):
        self._html = html

    def _get_links_from_html(self):
        # TODO: refactor to use new attribute methods
        doc = pq(self._html)
        anchor_elements = doc('a')
        anchor_hrefs = []
        for el in anchor_elements:
            anchor_hrefs.append(pq(el).attr['href'])
        return anchor_hrefs

    def _get_attribute_from_element(self, attribute, element):
        """
        Takes an attribute to search for (string) and an lxml.etree.Element
        object
        """
        return pq(element).attr[attribute]

    def _get_attribute_list_from_element_list(self, attribute, element_list):
        """
        Takes an attribute to search for (string) and a list of elements as a
        PyQuery object
        """
        attr_list = []
        for e in element_list:
            attr = self._get_attribute_from_element(attribute, e)
            if attr is not None:
                attr_list.append(attr)
        return attr_list

    def _get_assets_from_html(self):

        assets = []

        doc = pq(self._html)

        a_elements = doc('a')
        link_elements = doc('link')
        img_elements = doc('img')
        script_elements = doc('script')

        assets = assets + self._get_attribute_list_from_element_list(
            'href', a_elements)
        assets = assets + self._get_attribute_list_from_element_list(
            'href', link_elements)
        assets = assets + self._get_attribute_list_from_element_list(
            'src', img_elements)
        assets = assets + self._get_attribute_list_from_element_list(
            'src', script_elements)

        return assets

    @property
    def links(self):
        return self._get_links_from_html()

    @property
    def assets(self):
        return self._get_assets_from_html()
