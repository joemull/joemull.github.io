from glob import glob
import os

import ark
import lightningcss
from minify_html import minify


DEBUG = os.environ.get("DEBUG")
lightningcss.calc_parser_flags(nesting=True)


def format_html(html):
    if DEBUG:
        return html
    else:
        return minify(html)


def format_css(css):
    # Use lightningcss independently of minify_html
    # for greater control.
    if DEBUG:
        return css
    else:
        return lightningcss.process_stylesheet(
            css,
            filename="abc.css",
            browsers_list=["defaults"],
        )


out = ark.site.out()
patterns_and_functions = [
    (f"{out}/**/*.html", format_html),
    (f"{out}/**/*.css", format_css),
]


@ark.events.register(ark.events.Event.MAIN_BUILD)
def minify_out_files():
    for pattern, func in patterns_and_functions:
        for file in glob(pattern, recursive=True):
            with open(file, "r") as read_ref:
                formatted_text = func(read_ref.read())
            with open(file, "w") as write_ref:
                write_ref.write(formatted_text)
