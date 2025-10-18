from string import whitespace
from tablerpy import OutlineIcon, get_icon
from xml.etree import ElementTree
from minify_html import minify


# SVG namespace
ElementTree.register_namespace("", "http://www.w3.org/2000/svg")


# Jinja filters
def icon(icon_name, a11y_title):
    """
    A Jinja filter for inserting an SVG Tabler icon.
    """
    tablerpy_name = icon_name.replace("-", "_").upper()
    icon_path = get_icon(getattr(OutlineIcon, tablerpy_name))
    with open(icon_path, "rt") as icon_ref:
        svg_string = icon_ref.read()
        root = ElementTree.fromstring(svg_string)
        root.set("height", "0.9em")
        root.set("width", "0.9em")
        title = ElementTree.fromstring(f"<title>{a11y_title}</title>")
        root.insert(0, title)
        svg = ElementTree.tostring(root, encoding="unicode")
    return minify(svg, keep_closing_tags=True)


def h2_and_rest(markdown):
    """
    Gets a leading h2 off of a Markdown block.
    """
    markdown = markdown.lstrip(whitespace)
    if markdown.startswith("##"):
        h2 = markdown.split("\n")[0]
        rest = markdown.replace(h2, "").strip(whitespace)
        return h2, rest
    else:
        return "", markdown
