import re
from urllib.parse import urlparse

import ark
import jinja2
from marko import Markdown
from marko.ext.gfm import GFM
from marko.helpers import MarkoExtension
from filters import icon, h2_and_rest


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
