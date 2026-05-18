from string import whitespace
from xml.etree import ElementTree

import ark
from minify_html import minify
from tablerpy import OutlineIcon, get_icon


# Jinja filters
def icon(icon_name: str, a11y_title: str) -> str:
    """
    A Jinja filter for inserting an SVG Tabler icon.
    """
    ElementTree.register_namespace("", "http://www.w3.org/2000/svg")
    tablerpy_name = icon_name.replace("-", "_").upper()
    try:
        icon_path = str(get_icon(getattr(OutlineIcon, tablerpy_name)))
    except AttributeError:
        return ""
    with open(icon_path, "rt") as icon_ref:
        svg_string = icon_ref.read()
        root = ElementTree.fromstring(svg_string)
        root.set("height", "0.9em")
        root.set("width", "0.9em")
        title = ElementTree.fromstring(f"<title>{a11y_title}</title>")
        root.insert(0, title)
        svg = ElementTree.tostring(root, encoding="unicode")
        return minify(svg, keep_closing_tags=True)


def heading_and_rest(markdown: str) -> tuple[str, str]:
    """
    Gets a leading h2 or h3 off of a Markdown block.
    """
    markdown = markdown.lstrip(whitespace)
    if markdown.startswith("##"):
        heading = markdown.split("\n")[0]
        rest = markdown.replace(heading, "").strip(whitespace)
        return heading, rest
    else:
        return "", markdown


@ark.events.register(ark.events.Event.INIT)
def load_jinja_filters() -> None:
    import ark_jinja

    ark_jinja.jinja_environment.filters["icon"] = icon
    ark_jinja.jinja_environment.filters["heading_and_rest"] = heading_and_rest
