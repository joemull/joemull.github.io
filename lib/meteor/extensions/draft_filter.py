import os

import ark


@ark.filters.register(ark.filters.Filter.LOAD_NODE_FILE)
def filter_drafts(whether_to_render, file_path):
    DRAFTS = os.environ.get("DRAFTS")
    if file_path.stem.endswith("--draft") and not DRAFTS:
        whether_to_render = False
    return whether_to_render
