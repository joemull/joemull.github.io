import ark
import jinja2
from xml.etree import ElementTree
from tablerpy import OutlineIcon, get_icon

jinja_environment = None
ElementTree.register_namespace("", "http://www.w3.org/2000/svg")


def icon(icon_name, a11y_title):
    """
    A filter for inserting an SVG Tabler icon.
    """
    tablerpy_name = icon_name.replace("-", "_").upper()
    icon_path = get_icon(getattr(OutlineIcon, tablerpy_name))
    with open(icon_path, "rt") as icon_ref:
        svg_string = icon_ref.read()
        root = ElementTree.fromstring(svg_string)
        root.insert(0, ElementTree.fromstring(f"<title>{a11y_title}</title>"))
    return ElementTree.tostring(root, encoding="unicode")


@ark.events.register(ark.events.Event.INIT)
def initialize_jinja_environment():
    settings = {
        "loader": jinja2.FileSystemLoader(ark.site.theme("templates")),
    }
    settings.update(ark.site.config.get("jinja_settings", {}))
    global jinja_environment
    jinja_environment = jinja2.Environment(**settings)
    jinja_environment.filters["icon"] = icon


@ark.filters.register(ark.filters.Filter.NODE_TEXT)
def prerender_jinja(text, node):
    """
    Apply Jinja to the source Markdown files, so that you can
    use Jinja template syntax, tags, and filters in source content.
    """
    template = jinja_environment.from_string(text)
    text_after_jinja = template.render({})
    return text_after_jinja


@ark.templates.register("jinja")
def render_page(page_data, template_filename):
    template = jinja_environment.get_template(template_filename)
    return template.render(page_data)
