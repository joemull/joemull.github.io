import os
import pathlib

import ark

ark.site.init()
extensions = ark.site.theme("extensions")


def test_typography_em_dash():
    ark.extensions.load_module(extensions, "typography")
    result = ark.filters.apply("node_text", "hi--bye", None)
    assert result == "hi—bye"


def test_format_html():
    from lib.meteor.extensions import minify

    result = minify.format_html('<p  class=" crispy">apple</p>\n <p>pear</p>')
    assert result == "<p class=crispy>apple</p><p>pear</p>"


def test_format_css():
    from lib.meteor.extensions import minify

    result = minify.format_css(
        "body {  \n color: #000; abbr {  display:  none; background: blue; } }"
    )
    assert result == "body{color:#000}body abbr{background:#00f;display:none}"


def test_filter_drafts(monkeypatch):
    ark.extensions.load_module(extensions, "draft_filter")
    path = pathlib.Path("something/not-ready--draft.md")

    monkeypatch.setenv("DRAFTS", "true")
    whether_to_render = ark.filters.apply("load_node_file", True, path)
    assert whether_to_render

    monkeypatch.setenv("DRAFTS", "")
    whether_to_render = ark.filters.apply("load_node_file", True, path)
    assert not whether_to_render

    monkeypatch.delenv("DRAFTS")
    whether_to_render = ark.filters.apply("load_node_file", True, path)
    assert not whether_to_render


def test_icon():
    from lib.meteor.extensions import renderer

    icon = renderer.icon("cat", "Cat icon")
    assert icon.startswith("<svg")


def test_prerender_jinja():
    ark.extensions.load_module(extensions, "renderer")
    ark.events.fire(ark.events.Event.INIT)
    result = ark.filters.apply("node_text", "{{ 'jinja' }}", None)
    assert result == "jinja"


def test_render_link_internal():
    ark.extensions.load_module(extensions, "renderer")
    ark.events.fire(ark.events.Event.INIT)
    text = "[My link](/path/to/link)"
    result = ark.renderers.render(text, "md")
    assert "<a" in result
    assert "<svg" not in result
    assert "opens in new tab" not in result


def test_render_link_external():
    ark.extensions.load_module(extensions, "renderer")
    ark.events.fire(ark.events.Event.INIT)
    text = "[My link](https://www.example.org/path/to/link)"
    result = ark.renderers.render(text, "md")
    assert "<a" in result
    assert "<svg" in result
    assert "opens in new tab" in result
