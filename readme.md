# Development

## Installation

Install a Python virtual environment and install requirements.

Install bun and install the lock file dependencies.

## Worfklows

To make small changes:

```
ark watch
```

To avoid minifying HTML and CSS:

```
DEBUG="true" ark watch
```

To clear the directory before writing:

```
ark watch -c
```

To include drafts saved with filename suffix `--draft.md`:

```
DRAFTS="true" ark watch
```

To run formatting and linting:

```
ruff format --check .
bun x prettier --check .
```

To install pre-commmit hooks for formatting and linting:

```
git config --local core.hooksPath .git-hooks
```
