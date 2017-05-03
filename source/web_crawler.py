import requests
import sys
from pyquery import PyQuery as pq
from urllib.parse import urlparse, urljoin


def make_request(url):
  r = requests.get(url)
  return r

def get_anchor_hrefs_from_html_string(string):
  doc = pq(string)
  anchor_elements = doc('a')
  anchor_hrefs = []
  for e in anchor_elements:
    anchor_hrefs.append(pq(e).attr['href'])
  return anchor_hrefs

def link_belongs_to_domain(link, domain):
  parsed = urlparse(link)
  return domain == parsed.netloc

def validate_argument_count(args):
  if len(args) == 2:
    return True
  else:
    raise SystemExit('Too many arguments')

def get_absolute_links(url, link_list):
  absolute_links = []
  for link in link_list:
    absolute_links.append(urljoin(url, link))
  return absolute_links

def get_links_internal_to_domain(links, domain):
  internal_links = []
  for link in links:
    if link_belongs_to_domain(link, domain):
      internal_links.append(link)
  return internal_links

def get_internal_links_from_url(url):
  domain = urlparse(url).netloc
  response = make_request(url)
  anchor_hrefs = get_anchor_hrefs_from_html_string(response.text)
  absolute_link_list = get_absolute_links(url, anchor_hrefs)
  internal_links = get_links_internal_to_domain(absolute_link_list, domain)
  return internal_links

def crawl(url):
  internal_links = get_internal_links_from_url(url)
  for link in internal_links:
    print(link)

def main():
  validate_argument_count(sys.argv)
  crawl(sys.argv[1])

if __name__ == '__main__':
  main()
