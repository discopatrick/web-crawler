import requests
import sys
from pyquery import PyQuery as pq
from urllib.parse import urlparse, urljoin


found = []
crawled = []

def make_request(url):
  try:
    r = requests.get(url)
    return r
  except requests.exceptions.MissingSchema:
    return None

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

def uniquify(seq):
  """
  Takes a sequence and quickly removes duplicates
  http://stackoverflow.com/a/480227/3293805
  """
  seen = set()
  seen_add = seen.add
  return [x for x in seq if not (x in seen or seen_add(x))]

def remove_query_and_fragment(link_list):
  processed_list = []
  for link in link_list:
    p = urlparse(link)
    new_link = p.netloc + p.path
    if p.scheme != '':
      new_link = p.scheme + '://' + new_link
    processed_list.append(new_link)
  return processed_list

def get_internal_links_from_url(url):
  domain = urlparse(url).netloc
  response = make_request(url)
  if response is None:
    return []
  links = get_anchor_hrefs_from_html_string(response.text)
  links = uniquify(links)
  links = get_absolute_links(url, links)
  links = remove_query_and_fragment(links)
  links = get_links_internal_to_domain(links, domain)
  return links

def crawl(url):
  internal_links = get_internal_links_from_url(url)
  if internal_links:
    for link in internal_links:
      if link not in crawled:
        if link not in found:
          found.append(link)

  for link in found:
    found.remove(link)
    if link not in crawled:
      print(link)
      crawled.append(link)
      crawl(link)

def main():
  validate_argument_count(sys.argv)
  crawl(sys.argv[1])
  print('{} link(s) crawled'.format(len(crawled)))

if __name__ == '__main__':
  main()
