import os
from pathlib import Path

import ark


@ark.filters.register(ark.filters.Filter.LOAD_NODE_FILE)
def filter_drafts(whether_to_render: bool, file_path: type[Path]) -> bool:
    DRAFTS = os.environ.get("DRAFTS")
    if str(file_path.stem).endswith("--draft") and not DRAFTS:
        whether_to_render = False
    return whether_to_render
