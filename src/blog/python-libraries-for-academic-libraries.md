---
title: Python libraries for academic libraries
date: 2023-10-14
---

Before I started working on web applications, I mainly used Python to curate digital collections and metadata.

Some people call it _data wrangling_, as if academic libraries were Texas cattle ranches full of mooing CSVs. Others call it data manipulation, data management, or just scripting. I am partial to _data curation_--a bit highbrow, but descriptive of the care that goes into this work: touching up, checking for infelicities and fixing them, and recognizing opportunities for enrichment and synthesis.

If you want a graphical interface for this work, you can use the free and open-source [OpenRefine](https://openrefine.org/) desktop app. I often use OpenRefine when I want fast results or want to explore an unfamiliar dataset visually.

For greater control and flexibility, you can write Python scripts. This may sound like more work, but often it is less. Because the Python ecosystem is vast and rich beyond imagining, it is likely that someone else has solved your problem before you. Some absolute saint with more time and, let’s face it, more brain cells has created a free and open-source Python library in exactly the same niche as yours. By learning and using these libraries, you can abstract away the tedious setup routine and fiendish details and just focus on caring for your dataset and your users.

## OCRmyPDF

Whenever I work with PDFs, I reach for this utility. It is especially wondrous for PDFs created with a scanner, since those typically do not have embedded text, just images of the printed page, meaning no one can search them or access their content via text-to-speech.

The [OCRmyPDF](https://ocrmypdf.readthedocs.io) utility has ten thousand GitHub stars, excellent documentation, and a flawless API. Under the hood, it uses Tesseract OCR, an engine built by HP and Google before becoming community-maintained in 2018.

Not only will OCRmyPDF give you exactly the copy-paste experience and machine readability you need, it will respectfully optimize the files and bring them up to [PDF/A](https://en.wikipedia.org/wiki/PDF/A), the ISO PDF standard for archival preservation.

This little library even seems to know more about your PDFs than they know about themselves, because if you give it corrupt or borked PDFs (whether or not they need OCR), it magically fixes them. I have turned to it more than once when doing tech support to fix just one stubborn file.

## isbnlib

I once had a list of ISBNs of questionable origin. They had been manually entered, with inconsistent formatting, in both 10-digit and 13-digit variations. Some had been pulled from the OCR of book front matter using regex.

I used [isbnlib](https://github.com/xlcnd/isbnlib) to standardize the format, flag invalid numbers, and otherwise prep them for selective manual checks.

The convenience of this library comes especially in its ability to detect the input format and output a canonical 13-digit format.

## diskcache

If I ever have to write a script that spends a lot of time on one network, whether by using a REST API or by scraping a set of content pages, I always start by implementing caching at the level of the HTTP request. This way I avoid hitting any endpoint more than once, no matter how many times I need to change and rerun my script to get the desired result.

My favorite caching tool is [diskcache](https://grantjenks.com/docs/diskcache/), which provides a dead-simple API and handles caching via a SQLite database in the background. I generally use the request URL as the cache key.

## tqdm

Of the nine, this library feels the most magical, because you only have to type four letters to use it. Wrap any iterable with `tqdm()`, and your terminal will have progress bars that show the iterations.

## BeautifulSoup

When I have needed to migrate a collection from one system to another, I have often needed to pull metadata out of HTML or XML documents.

[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) lets you load the document into a Python object tree kind of like the document object model (DOM) used by web browsers, to query and manipulate it.

An honourable mention here is the lxml library (or in-built Python `xml` module) that allows more advanced work with XML. By convention, you get to use the acronym ET, for `ElementTree`, one of the library’s main classes. But to use this one well, you really want to be up on your namespace management, XPath syntax, and semantic whitespace rules. I usually turn to BeautifulSoup first, and only if I need 1-mil tolerances do I fire up the big boy.

## pandas

Python’s built-in CSV library is fine. It does the job. But if you regularly work with tabular data in Python scripts, it is worth learning [pandas](https://pandas.pydata.org/). (Or one of the newer alternatives for working with data frames, like [polars](https://docs.pola.rs/).

I admit it was time consuming for me to learn this solo. I found the learning curve to be steep, because I had to unlearn some habits. For example, iteration is usually not the best pattern for doing something with each cell of a column. But once you learn the patterns for working with data frames, they are very powerful and much more flexible than what you have with the built-in CSV library.

One small thing I loved about pandas: it has an excellent API for opening and saving in both CSV and spreadsheets in XLSX format. This means you don’t have to manually export as CSV before working on something produced in Excel. You can also automatically format every output so that it has a few nice display features, like bolding and color coding, right when you first open it up in Excel. This was a big bonus for me, since I was producing data that would be consumed by others, and I wanted the spreadsheet to look nice.

## pypandoc

Pandoc is a “universal document converter” written in Haskell, a niche language optimised for functional programming. You can use it as a [command line tool](https://pandoc.org/installing.html) if you do not need to inscribe a process in a script.

Fortunately there is also a Python wrapper, [pypandoc](https://github.com/JessicaTegner/pypandoc), which allows you to use it in a Python script, and which allows me to include it on this Python-centric list.

When I found out Pandoc was written by a tenured Berkeley philosophy professor in his spare time, I thought, “this guy knows,” and was immediately in its thrall. The audacity of the word “universal” and the sheer doggedness of Pandoc’s implementation inspire me to no end.

I mostly use Pandoc for producing MS Word or HTML output from Markdown, but it can handle dozens of other format combinations.

At some point, the promise of universal conversion does break down, because each markup schema exists for its own reasons, and eventually those reasons clash. But the distance you can go is still impressive and very useful.

## python-docx

The day I realised I could read and write Word documents in Python, I nearly fell out of my chair.

Until 2007, Microsoft Word saved files in a proprietary binary format with a `.doc` extension. But in the 2000s, they developed an XML standard and convinced about eight other companies and several national libraries to agree with them on an open schema.

Since then, Word files have generally been saved with a `.docx` extension, which is not a binary file but a zip file containing XML files. That means that DOCX files, like any other kind of XML, can be accessed and represented in Python.

The [python-docx](https://python-docx.readthedocs.io) library provides utilities for interacting with DOCX files. It is partial, given how sprawling the Office Open XML standard is, but it is high-quality, with rigorous engineering and testing standards.

## rdflib

In you work with linked data, get to know rdflib. You can start with a CSV in the morning and be spitting out Turtle files by sundown.

This library lets you work with RDF graphs in Python, and serialize to and from RDF/XML, Turtle, and JSON-LD, among others.
