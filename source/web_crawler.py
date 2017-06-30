import sys
from urllib.parse import urlparse

from .lib import Crawler, Url

def validate_argument_count(args):
    if len(args) < 2:
        raise SystemExit('Not enough arguments')
    elif len(args) == 2:
        return True
    else:
        raise SystemExit('Too many arguments')

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

# TODO: use this format for final output
# def crawl(url):
#
#     print('[page] ' + url)
#
#     assets = get_assets(response.text, url)
#
#     if assets:
#         for asset in assets:
#             print('       - ' + asset)
#     else:
#         print('       - (no assets)')

def main():
    validate_argument_count(sys.argv)
    crawler = Crawler(sys.argv[1])
    crawler.crawl()
    print('{} link(s) crawled'.format(crawler.crawled_count()))
