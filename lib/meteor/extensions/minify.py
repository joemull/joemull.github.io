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
        return minify(
            html,
            keep_html_and_head_opening_tags=True,
            keep_closing_tags=True,
        )


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
html_patterns = [
    f"{out}/**/*.html",
]
css_patterns_and_outputs = [
    ([f"{out}/components/*.css"], f"{out}/components.min.css"),
    ([f"{out}/slide_components/*.css"], f"{out}/slide_components.min.css"),
    ([f"{out}/utilities.css"], f"{out}/utilities.min.css"),
    (
        [f"{out}/**/reset.css", f"{out}/**/settings.css", f"{out}/**/*.css"],
        f"{out}/base.min.css",
    ),
]


@ark.events.register(ark.events.Event.MAIN_BUILD)
def minify_html():
    for pattern in html_patterns:
        for file in glob(pattern, recursive=True):
            with open(file, "r") as read_ref:
                formatted_text = format_html(read_ref.read())
            with open(file, "w") as write_ref:
                write_ref.write(formatted_text)


@ark.events.register(ark.events.Event.MAIN_BUILD)
def minify_css():
    files_to_write = []
    outputs = set(output for _, output in css_patterns_and_outputs)
    for patterns, output in css_patterns_and_outputs:
        formatted_text = ""
        for pattern in patterns:
            for file in glob(pattern, recursive=True):
                if file not in outputs:
                    with open(file, "r") as read_ref:
                        if DEBUG:
                            formatted_text += "\n\n"
                        formatted_text += format_css(read_ref.read())
                os.remove(file)
        files_to_write.append((formatted_text, output))
    for formatted_text, output in files_to_write:
        with open(output, "w") as write_ref:
            write_ref.write(formatted_text)
