import ark
from marko.ext.gfm import gfm


@ark.renderers.register("md")
def render_markdown(text):
    return gfm.convert(text)
