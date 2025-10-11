# ------------------------- #
#  Site Configuration File  #
# ------------------------- #

import os

# Variables set here will be available in template files under a `site` attribute,
# e.g. {{ site.title }}.

# Choose the theme to use when building your site. This variable should specify
# the name of a theme directory in your site's 'lib' folder.
theme = "meteor"

# Site title.
title = "Joe Muller"

# Site tagline.
# tagline = ""

# Default author
default_author = "Joe Muller"

# Domain for refernce links on PDF slidedecks
if os.environ.get("DEBUG"):
    homepage = "http://localhost:8080/"
else:
    homepage = "https://joemull.net/"

# Language
lang = "en-US"

# Extensions
extensions = [
    "holly",
]

# Blog extension
holly = {
    "roots": [
        {"root_url": "@root/blog//"},
        {"root_url": "@root/slides//"},
    ],
    "homepage": {
        "root_urls": ["@root/blog//"],
    },
}

# Jinja settings
jinja_settings = {
    "trim_blocks": True,
    "lstrip_blocks": True,
}

# RSS settings
rss_root_urls = ["@root/blog//"]
