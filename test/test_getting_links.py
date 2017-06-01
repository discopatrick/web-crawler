from unittest import TestCase
from pyquery import PyQuery as pq
from source.web_crawler import *


class LinkGetterTest(TestCase):

    def test_get_anchor_hrefs_from_html_string(self):
        html = """
      <html>
        <head>
          <title>My Page</title>
        </head>
        <body>
          <h1>My Page</h1>
          <p>Search for stuff at <a href="http://www.google.co.uk">Google</a></p>
          <p>Fritter your life away at <a href="http://www.facebook.com">Facebook</a></p>
        </body>
      </html>
    """
        anchor_hrefs = get_anchor_hrefs_from_html_string(html)

        self.assertEqual(len(anchor_hrefs), 2)

    def test_link_belongs_to_domain(self):

        domain = 'www.bbc.co.uk'
        link_from_domain = 'http://www.bbc.co.uk/contact-us/'
        link_outside_domain = 'http://www.facebook.com/faq/'

        self.assertTrue(link_belongs_to_domain(link_from_domain, domain))
        self.assertFalse(link_belongs_to_domain(link_outside_domain, domain))

    def test_get_absolute_links(self):

        base_url = "http://www.example.com/a/b.html"
        link_list = [
            "http://www.example.com/c/d.html",
            "/e/f.html",
            "g/h.html",
            "./i.html",
            "../j.html"
        ]
        expected_list = [
            "http://www.example.com/c/d.html",
            "http://www.example.com/e/f.html",
            "http://www.example.com/a/g/h.html",
            "http://www.example.com/a/i.html",
            "http://www.example.com/j.html",
        ]

        absolute_links = get_absolute_links(base_url, link_list)

        self.assertEqual(absolute_links, expected_list)

    def test_remove_query_and_fragment(self):

        link_list = [
            "http://www.example.com/a?b=c#f",
            "www.example.com/a?b=c#f",
        ]
        expected_list = [
            "http://www.example.com/a",
            "www.example.com/a",
        ]

        processed_list = remove_query_and_fragment(link_list)

        self.assertEqual(processed_list, expected_list)


class AssetGetterTest(TestCase):

    def test_get_attribute_from_element(self):
        html = """
      <p>Search for stuff at <a href="http://www.google.co.uk">Google</a></p>
      <p>Fritter your life away at <a href="http://www.facebook.com">Facebook</a></p>
    """

        doc = pq(html)
        a_elements = doc('a')

        attr = get_attribute_from_element('href', a_elements[0])

        self.assertEqual(attr, 'http://www.google.co.uk')
