import requests
import sys
from pyquery import PyQuery as pq
from urllib.parse import urlparse, urljoin


touched = []
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

def get_links_internal_to_domain(link_list, domain):
  internal_links = []
  for link in link_list:
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

def get_attribute_from_element(attribute, element):
  """
  Takes an attribute to search for (string) and an lxml.etree.Element object
  """
  return pq(element).attr[attribute]

def get_attribute_list_from_element_list(attribute, element_list):
  """
  Takes an attribute to search for (string) and a list
  of elements as a PyQuery object
  """
  attr_list = []
  for e in element_list:
    attr = get_attribute_from_element(attribute, e)
    if attr is not None:
      attr_list.append(attr)
  return attr_list
  
def get_assets(html):
  assets = []

  doc = pq(html)
  
  a_elements = doc('a')
  link_elements = doc('link')
  img_elements = doc('img')
  script_elements = doc('script')

  assets = assets + get_attribute_list_from_element_list('href', a_elements)
  assets = assets + get_attribute_list_from_element_list('href', link_elements)
  assets = assets + get_attribute_list_from_element_list('src', img_elements)
  assets = assets + get_attribute_list_from_element_list('src', script_elements) 

  return assets

def crawl(url):
  touched.append(url)

  response = make_request(url)
  if response.headers['content-type'] != 'text/html':
    return

  print('[page] ' + url)

  assets = get_assets(response.text)
  if assets:
    for asset in get_assets(response.text):
      print('       - ' + asset)
  else:
    print('       - (no assets)')

  internal_links = get_internal_links_from_url(url)

  if internal_links:
    for link in internal_links:
      if link not in touched:
        crawl(link)

  crawled.append(url)

def main():
  validate_argument_count(sys.argv)
  crawl(sys.argv[1])
  print('{} link(s) crawled'.format(len(crawled)))

if __name__ == '__main__':
  main()
