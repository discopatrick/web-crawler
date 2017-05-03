from unittest import TestCase
from source.web_crawler import *

class LinkGetterTest(TestCase):

  def test_get_links_from_string(self):
    string = """
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
    
    links = get_links_from_string(string)

    self.assertEqual(len(links), 2)
