import requests
from pyquery import PyQuery as pq


def make_request(url):
  r = requests.get(url)
  return r

def get_links_from_string(string):
  doc = pq(string)
  links = doc('a')
  return links
