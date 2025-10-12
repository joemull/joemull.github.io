import datetime
import hashlib
import uuid
from xml.etree import ElementTree

import ark
import holly
import os
from feedgenerator import Atom1Feed
from jinja2 import filters


def get_child_nodes(feed, node):
    nodes = []
    for child in node.children:
        if child.has_children:
            nodes.extend(get_child_nodes(feed, child))
        elif not child.get("is_tag_base") and not child.get("is_tag_index"):
            nodes.append(child)
    return nodes


def get_nodes(feed):
    nodes = []
    for root_url in ark.site.config.get("rss_root_urls", []):
        node = ark.nodes.node(root_url)
        nodes.extend(get_child_nodes(feed, node))
        default_date = datetime.date(2000, 1, 1)
        nodes.sort(key=lambda node: node.filepath)
        nodes.sort(key=lambda node: node.get("date") or default_date, reverse=True)
        nodes = nodes[:10]
    return nodes


def get_ark_node_description(node):
    stripped = filters.do_striptags(node.html)
    truncated = stripped[:97].rsplit(" ", 1)[0] + "..."
    return truncated


def insert_icon(xml, favicon_url):
    ElementTree.register_namespace("", "http://www.w3.org/2005/Atom")
    root = ElementTree.fromstring(xml)
    icon = ElementTree.fromstring(f"<icon>{favicon_url}</icon>")
    root.insert(0, icon)
    xml = ElementTree.tostring(root, encoding="unicode")
    return xml


@ark.events.register(ark.events.Event.EXIT_BUILD)
def generate_feed():
    config = ark.site.config
    title = config.get("title", "")
    relative_link = "feed.xml"
    description = filters.do_striptags(
        ark.site.includes().get("site_description", ""),
    )
    homepage = config.get("homepage", "")
    if not homepage:
        raise Exception(
            "There must be a homepage specified in config.py to generate the RSS feed."
        )
    rss_link = os.path.join(homepage, relative_link)
    feed = Atom1Feed(
        title=title,
        link=rss_link,
        description=description,
        language=config.get("lang"),
    )
    nodes = get_nodes(feed)
    path = ark.site.out(relative_link)
    for node in nodes:
        author = node.get("author") or config.get("default_author", "")
        node_path = ark.utils.rewrite_urls(f"'{node.url}'", path).strip("'")
        url = os.path.join(homepage, node_path)
        item_license = config.get("default_license", "")
        feed.add_item(
            title=node.get("title"),
            author_name=author,
            link=url,
            description=get_ark_node_description(node),
            pubdate=node.get("date"),
            content=node.html,
        )

    xml = feed.writeString("utf-8")
    favicon_path = ark.utils.rewrite_urls(f"'@root/images/favicon.svg'", path)
    favicon_url = os.path.join(homepage, favicon_path.strip("'"))
    xml = insert_icon(xml, favicon_url)

    xml = ark.utils.rewrite_urls(xml, path)
    if not os.path.isdir(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    with open(path, "w") as file:
        file.write(xml)
