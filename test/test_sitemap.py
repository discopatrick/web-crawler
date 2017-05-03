from unittest import TestCase
from source.web_crawler import *

class SitemapTest(TestCase):

  def test_get_link_list(self):
    
    links = [
      '<a href="http://www.google.co.uk">Google</a>',
      '<a href="http://www.facebook.com">Facebook</a>'
    ]

    expected_output = """
http://www.google.co.uk
http://www.facebook.com
"""

    actual_output = get_link_list_from_links(links)

    self.assertEqual(expected_output, actual_output)
