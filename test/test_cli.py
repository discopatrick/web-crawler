from unittest import TestCase
from source.web_crawler import *

class CLITest(TestCase):

  def test_validate_argument_count_returns_true_with_2_args(self):
    args = ['source/web_crawler.py', 'http://www.bbc.co.uk']
    result = validate_argument_count(args)

    self.assertTrue(result)

  def test_validate_argument_count_raises_error_when_not_2_args(self):
    args = ['source/web_crawler.py', 'http://www.bbc.co.uk', 'rogue-argument']

    with self.assertRaises(SystemExit):
      validate_argument_count(args)
