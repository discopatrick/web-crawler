import requests

def make_request(url):
  r = requests.get(url)
  return r

def get_links_from_string(string):
  links = []
  links.append('http://www.google.co.uk')
  return links
