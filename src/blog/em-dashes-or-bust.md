---
title: Em dashes or bust
date: 2025-10-18
---

On the whole, I’d like this blog to be about more than this blog, but today I am indulging a bit.

I want to talk about how I write em dashes. Such a simple thing, yet in a Markdown authoring environment, it is not simple, at least when I am the author. I prefer to press the hyphen key twice to produce “--” and have my software convert it to the Unicode character for an em dash for me. I can’t be asked to remember a key combination to get the Unicode character while writing. I use Vim on Linux, I use a Bluetooth keyboard that has a slightly different layout than my laptop keyboard, and I also have to switch between US and UK layouts, so it is just not worth it. I also do not want to copy-paste an em dash from elsewhere into my Markdown every time I need one.

I would much rather write a regular-expression-based extension to my static site generator and then blog about it. Because not only does this give me an opportunity to announce myself as an em-dash-lord, I can also fanboy about the Ark site generator and the eternal marvels of regular expressions.

## The static site generator

[Ark](https://www.dmulholl.com/docs/ark/master/) by Darren Mulholland is the static site generator I use for this site. It has a nice and simple system for extensions, letting me hook into the parsing and rendering pipeline at key points to read and modify the content in the way I want.

All I have to do is create a file in my theme’s `extensions` folder and write a function with an Ark-provided decorator.

```py
import ark

@ark.filters.register(ark.filters.Filter.NODE_TEXT)
def em_dash(text, node):
   ...
   return modified_text
```

The `node_text` filter is applied right before Ark does the rendering of the source text into HTML, in `Node.html`:

```py
class Node():
    ...
    def html(self) -> str:
        if not 'html' in self.cache:
            text = filters.apply('node_text', self.text, self)
            html = renderers.render(text, self.ext, self.filepath)
```

In addition to the text as a string, the function receives the `Node` instance. A node is Ark’s container for metadata and information about how the file relates to others in the content hierarchy. Sometimes reading or writing to the node’s data is key, but in this case, I do not need this object at all.

All I need is the text, because I just need to find the em dashes I’ve authored in Markdown and replace them with the fancy Unicode character.

## The regular expression

What [regular expression](https://docs.python.org/3/library/re.html) can identify an em dash? It depends on how the author writes em dashes, so writing general-purpose regex for this would be tricky. But if I am just writing for my own usage, it is not hard to encode. I only use em dashes to change direction in the middle of a sentence.

Another thing--I never put spaces around an em dash. (I mean, to be honest, the fact that you had to ask exposes you as a philistine, because space around an em dash is pure sacrilege.) Luckily, pedantry actually makes things easier in this case, because I can be pickier about the characters that precede or follow the dash, excluding whitespace or line breaks, and so avoiding horizontal rules, YAML block delimiters, or who knows what else.

```py
import re

TWO_HYPHEN_DASH = re.compile(
    r"(?<=[a-zA-Z\"'”’_\*])--(?=[a-zA-Z\"'“‘_\*])"
)
```

This expression matches two hyphens that are immediately preceded by, and followed by, a letter or quotation mark, or the Markdown symbols for italics or boldface.

The ideas of “preceded by” and “followed by” are handled by lookbehind and lookahead assertions, `(?<=...)` and `(?=...)`.

I include the symbols for both straight (`'`) and curly (`’`) quotes. I have a Vim plugin (`vim-textobj-quote`) that automatically changes straight to curly, based on the context.

Speaking of Vim plugins, why not just look for a plugin that changes the double hyphens in place, in the source file? Because I use a monospace font in Vim, and always will, and that would make any em dash look like a hyphen while I am writing, which would be distracting. The whole idea of an em dash is that it is longer than most characters--it's the width of an “M” in variable-width typefaces. The double dash looks more correct because it takes up double the space, so it’s the best thing to work with when writing.

## Putting it together

The complete extension is very short:

```py
import re
import ark

TWO_HYPHEN_DASH = re.compile(
    r"(?<=[a-zA-Z\"'”’_\*])--(?=[a-zA-Z\"'“‘_\*])"
)

@ark.filters.register(ark.filters.Filter.NODE_TEXT)
def em_dash(text, node):
    return re.sub(TWO_HYPHEN_DASH, "—", text)
```

Setting this up gave me no end of delight, because it closed a loop that Vim, which I otherwise love, had left open in my authoring environment. I have always used em dashes in my writing, and once upon a time, when I wrote in Word, I could see them in my drafts. When I started to write more non-code things in Vim, I searched out the tools to make it a nicer environment for English prose. I installed plugins like `vim-pencil` and `vim-textobj-quote`. This got me nearly all the way.

And now that my little horizontal lines between sentence fragments are the right length, Vim really does feel like home.
