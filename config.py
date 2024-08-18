# ------------------------- #
#  Site Configuration File  #
# ------------------------- #

# Variables set here will be available in template files under a `site` attribute,
# e.g. {{ site.title }}.

# Choose the theme to use when building your site. This variable should specify
# the name of a theme directory in your site's 'lib' folder.
theme = "canary"

# Site title.
title = "Joseph Muller"

# Site tagline.
tagline = "I write about tech and humanities and other things"

# Language
lang = 'en-US'

# Extensions
extensions = [
    'holly',
]

# Blog extension
holly = {
    "roots": [
        {"root_url": "@root/blog//"},
    ],
    "homepage": {
        "root_urls": ["@root/blog//"],
    }
}
