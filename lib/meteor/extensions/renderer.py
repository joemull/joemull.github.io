import re
from string import whitespace
from urllib.parse import urlparse
from xml.etree import ElementTree

import ark
import jinja2
from tablerpy import OutlineIcon, get_icon
from marko import Markdown
from marko.ext.gfm import GFM
from marko.helpers import MarkoExtension


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
        title = ElementTree.fromstring(f"<title>{a11y_title}</title>")
        root.insert(0, title)
        svg = ElementTree.tostring(root, encoding="unicode")
    return svg


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


# Jinja environment
jinja_environment = None


@ark.events.register(ark.events.Event.INIT)
def initialize_jinja_environment():
    settings = {
        "loader": jinja2.FileSystemLoader(ark.site.theme("templates")),
    }
    settings.update(ark.site.config.get("jinja_settings", {}))
    global jinja_environment
    jinja_environment = jinja2.Environment(**settings)
    jinja_environment.filters["icon"] = icon
    jinja_environment.filters["h2_and_rest"] = h2_and_rest


# Jinja prerender callback for Ark
@ark.filters.register(ark.filters.Filter.NODE_TEXT)
def prerender_jinja(text, node):
    """
    Apply Jinja to the source Markdown files, so that you can
    use Jinja template syntax, tags, and filters in source content.
    """
    template = jinja_environment.from_string(text)
    context = {
        "inc": ark.site.includes(),
    }
    text_after_jinja = template.render(context)
    return text_after_jinja


# Jinja render callback for Ark
@ark.templates.register("jinja")
def render_page(page_data, template_filename):
    template = jinja_environment.get_template(template_filename)
    return template.render(page_data)


# Marko extension
class MeteorRendererMixin(object):
    # Override the lists of escaped elements to omit `title` since it is used in inline SVGs
    tagfilter = re.compile(
        r"<(textarea|style|xmp|iframe|noembed|noframes|script|plaintext)",
        flags=re.I,
    )
    tagfilter_no_open = re.compile(
        r"(?<!^)( *)<(textarea|style|xmp|iframe|noembed|noframes|script|plaintext)",
        flags=re.I,
    )

    def render_link(self, element):
        # From overwritten function
        title = f' title="{self.escape_html(element.title)}"' if element.title else ""
        url = self.escape_url(element.dest)
        body = self.render_children(element)

        # New behavior
        context = {
            "is_external": bool(urlparse(url).netloc),
            "external_icon": True,
            "title": title,
            "url": url,
            "body": body,
        }
        template = jinja_environment.get_template(
            "components/rendered_link.jinja",
        )
        return template.render(context)


MeteorExtension = MarkoExtension(
    renderer_mixins=[MeteorRendererMixin],
)


# Marko renderer callback for Ark
@ark.renderers.register("md")
def render_markdown(text):
    markdown = Markdown(extensions=[GFM, MeteorExtension])
    return markdown(text)
