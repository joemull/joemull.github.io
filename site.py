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

# Linked data for JSON-LD
site_ttl = """
    @prefix sdo: <https://schema.org/>.
    <https://joemull.net> a sdo:WebSite,
            sdo:Blog;
        sdo:url "https://joemull.net";
        sdo:name "Joe Muller";
        sdo:author <https://orcid.org/0000-0003-3230-6090>;
        sdo:copyrightHolder <https://orcid.org/0000-0003-3230-6090>.
"""
author_ttl = """
    @prefix sdo: <https://schema.org/>.
    <https://orcid.org/0000-0003-3230-6090> a sdo:Person;
        sdo:sameAs "https://bsky.app/profile/joemull.zirk.us.ap.brid.gy",
            "https://bsky.app/profile/joemull.bsky.social",
            "https://zirk.us/@joemull",
            "https://github.com/joemull".
"""

# License
license = "https://creativecommons.org/licenses/by/4.0/"

# Domain for refernce links on PDF slidedecks
if os.environ.get("DEBUG"):
    homepage = "http://localhost:8080/"
else:
    homepage = "https://joemull.net/"

# Language
lang = "en"

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
