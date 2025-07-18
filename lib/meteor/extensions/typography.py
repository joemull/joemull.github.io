import re


import ark


# This identifies a two-hyphen dash, like --, surrounded by any plausible
# two characters, including letters and punctuation or markdown syntax that
# might feasibly be used on either side of the dash.
TWO_HYPHEN_DASH = re.compile(r"(?<=[a-z\"'”’_\*])--(?=[a-z\"'“‘_\*])")


@ark.filters.register(ark.filters.Filter.NODE_TEXT)
def em_dash(text, node):
    """
    Convert to hyphens with letters on either side to an em dash.
    """
    return re.sub(TWO_HYPHEN_DASH, "—", text)
