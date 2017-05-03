import requests
import sys
from pyquery import PyQuery as pq
from urllib.parse import urlparse


def make_request(url):
  r = requests.get(url)
  return r

def get_links_from_string(string):
  doc = pq(string)
  links = doc('a')
  return links

def get_link_list_from_links(links):
  output = '\n'
  for link in links:
    output += pq(link).attr['href'] + '\n'
  return output

def link_belongs_to_domain(link, domain):
  parsed = urlparse(link)
  return domain == parsed.netloc

def main():
  print('Hello Sitemap')
  for arg in sys.argv[1:]:
    print(arg)

if __name__ == '__main__':
  main()
