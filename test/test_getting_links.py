from unittest import TestCase
from pyquery import PyQuery as pq
from source.web_crawler import *


class LinkGetterTest(TestCase):

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
