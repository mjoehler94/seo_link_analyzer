from lxml import html


def get_urls_from_string(page_content: str, base_url: str) -> list:
    # note that base url can be added to make links absolute instead of from string
    tree = html.fromstring(page_content, base_url).make_links_absolute()
    links = [elem.get("href") for elem in tree.iter() if elem.tag() == "a"]
    return links
