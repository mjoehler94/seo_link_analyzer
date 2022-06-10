from lxml import html
from urllib.parse import urlparse


def get_urls_from_string(page_content: str, base_url: str) -> list:
    # note that base url can be added to make links absolute instead of from string
    tree = html.fromstring(page_content, base_url)
    tree.make_links_absolute()
    links = [elem.get("href") for elem in tree.iter() if elem.tag == "a"]
    return links

def normalize_url(url: str) -> str:
    parsed_url = urlparse(url)
    normalized = (parsed_url.netloc + parsed_url.path).lower().strip("/")
    return normalized
