---
title: What the ROR integration tells us about metadata in Janeway
date: 2026-05-21
type: slide_deck
title_footer: lower_decks_2026
theme: memory-alpha
---

{% from "slide_components/slide_grid_even_split.jinja" import slide_grid_even_split %}
{% from "slide_components/slide_focus.jinja" import slide_focus %}
{% from "slide_components/slide_text.jinja" import slide_text %}
{% from "slide_components/slide_title.jinja" import slide_title %}
{% from "slide_components/slide_frame.jinja" import slide_frame %}
{% from "slide_components/why_splat.jinja" import why_splat %}

{% call slide_text() %}

## In this talk

Main question: How can we help Janeway users create and manage high-quality metadata that includes URIs?

1. About ROR and Janeway
2. The five whys of URIs
3. Usability strategies for ROR features
4. Comparison to ORCID and DOI features
5. Takeaways
6. References

{%- endcall %}
{% call slide_focus() %}

## About ROR and Janeway

{%- endcall %}
{% call slide_grid_even_split() %}

## We integrated ROR into Janeway in 2024-25

<div class="flow">

![The ROR logo](@root/images/ror-icon-rgb.svg)

The Research Organization Registry is “a global, community-led registry of open persistent identifiers for research and funding organizations.”

</div>
<div class="flow">

User stories:

- “As an author I want to create and edit affiliations for me and my co-authors.”

- “As an editor I want to edit affiliations for authors.”

- “As an author or editor I want affiliations to be clear to readers and funders.”

</div>

{%- endcall %}
{% call slide_text() %}

## Searching to add an affiliation on Janeway

![A screenshot of the page in Janeway where you can search for an organization to add your affiliation.](@root/images/ror-blog-post-wcc.png)

{%- endcall %}
{% call slide_text() %}

## ROR on Janeway article page

![Screenshot showing an article page with a ROR-linked affiliation in the sidebar.](@root/images/ror-blog-post-walt-whitman-ui.png)

{%- endcall %}
{% call slide_text() %}

## ROR in Janeway-generated Crossref metadata

![Screenshot showing JSON Crossref metadata with a ROR-linked affiliation.](@root/images/ror-blog-post-crossref-json.png)

{%- endcall %}
{% call slide_focus() %}

## The five whys of URIs

{%- endcall %}
{% call slide_text() %}

## Hold on. Why?

We now have some links:

<div class="flex">

![Screenshot showing an article page with a ROR-linked affiliation in the sidebar.](@root/images/ror-blog-post-walt-whitman-ui-small.png)

![Screenshot showing JSON Crossref metadata with a ROR-linked affiliation.](@root/images/ror-blog-post-crossref-json-small.png)

</div>

{% call why_splat(n="1") %}

Why do we need them? Can’t authors just type their affiliations in and call it a day?

{% endcall %}

Five whys: ask why five times to discover the root cause of a problem.

Griff, my college English professor: “Why is it thus and not otherwise?”

{%- endcall %}
{% call slide_text() %}

## Organization names are re-usable and amorphous

<div class="grid grid-cols-2">
<div class="flow">

Three separate organizations on three continents:

| Name                 |
| -------------------- |
| Museum of Modern Art |
| Museum of Modern Art |
| Museum of Modern Art |

</div>
<div class="flow">

Three names for one organization:

| Name                             |
| -------------------------------- |
| University of Michigan–Ann Arbor |
| UMich                            |
| UM                               |

</div>
</div>

Also: misspelling, capitalization, punctuation, translation...

{% call why_splat(n="2") %}

Why do people do this?

{% endcall %}
{%- endcall %}
{% call slide_text() %}

## The vocabulary problem

In 1987, researchers at Bell Labs asked people to name things in several knowledge domains.

In most cases, people chose different words from each other.

> “The data tell us there is no one good access term for most objects. The idea of an ‘obvious,’ ‘self-evident,’ or ‘natural’ term is a myth!”

They called this the “vocabulary problem in human-system interaction.”

{% call why_splat(n="3") %}

Why is it worse when computers are involved?

{% endcall %}
{%- endcall %}
{% call slide_text() %}

## Banal context collapse

The scholarly record available through the World Wide Web is international and immense, and what you find there has been recontextualized by library discovery systems and search engines.

Problems caused:

- ambiguity - a word or phrase could refer to many things
- duplication - multiple records exist for a single thing
- retrieval failure - you don't always know the right search term
- outdated references - past names may be inaccurate

{% call why_splat(n="4") %}

Why does the Web contribute to these problems?

{% endcall %}
{%- endcall %}
{% call slide_text() %}

## The Web uses URLs

<div class="grid grid-cols-2 gap-2">
<div class="flow">

URLs are a ridiculously powerful vehicle. Their distinctive powers are:

- universality
- location

They can go get anything from any context (in theory) and put it next anything else.

</div>
<div class="flow">

![In a stadium at night, the words "This is for everyone" written in lights across the crowd](@root/images/this-is-for-everyone-olympic-stadium.png)

Web inventor Tim Berners-Lee's catchphrase "THIS IS FOR EVERYONE" at the 2012 olympics.

</div>
</div>

{% call why_splat(n="5") %}

I asked you about names. Why are we talking about links?

{% endcall %}

{%- endcall %}
{% call slide_text() %}

## Links are names

When URLs refer to things in the world, not just their own webpages, they are called _URIs_ or Uniform Resource _Identifiers_.

They are "identifiers" because they primarily identify the thing, and only secondarily point to a webpage about the thing.

<div class="fs-4 flow">

- https://orcid.org/0000-0001-7514-4920 universally identifies Gayatri Spivak.

- https://ror.org/04a1a1e81 universally identifies Dublin City University.

- https://doi.org/10.1145/32206.32212 universally identifies "The vocabulary problem in human-system communication".

</div>

{% call why_splat(n="?") %}

Using links as names is a _horrible idea_. They are too long and clunky. Can we shorten them at least?

{% endcall %}
{%- endcall %}
{% call slide_text() %}

## You need the whole thing

{{ inc.uri }}

There are other schemes, like `http` and `urn` and `ftp`.

The are lots of hosts. The host is a **namespace** managed by an institution (i.e. ROR) that guarantees the URI is distinct, persistent, and uniform.

The path is essential. It distinguishes this item from all the others like it.

{% call why_splat(n="?") %}

So we are stuck putting raw links everywhere?

{% endcall %}

{%- endcall %}
{% call slide_focus() %}

## Usability strategies for ROR features

{%- endcall %}
{% call slide_grid_even_split() %}

## Principles that shed light

<div class="flow">

In 1990 Jakob Nielsen began developing **usability heuristics** for interaction design.

Today "Nielsen's Ten" is still used as a checklist for noticing what's wrong with a user interface, and what's working well.

</div>

![An A4 size list of Nielsen's Ten Usability Heuristics](@root/images/nielsens-ten-a4-compressed.png)

{%- endcall %}
{% call slide_grid_even_split() %}

## Users search with the name they know

![Heuristic 2: Match between the system and the real world. The design should speak the users' language. Use words, phrases, and concepts familiar to the user, rather than internal jargon.](@root/images/nielsens-ten-02-with-example.png)

<div class="flow">

![The Janeway ROR search with the search term "Washtenaw" highlighted](@root/images/ror-blog-post-wcc-nielsen-02.png)

“Well, I know it has Washtenaw in it.”

</div>

{%- endcall %}
{% call slide_grid_even_split() %}

## Users don't edit the ROR ID or display name

![Heuristic 5: Error prevention. Good error message are important, but the best designs carefully prevent problems from occuring in the first place.](@root/images/nielsens-ten-05-with-example.png)

<div class="flow">

![The Janeway ROR search showing that name and ROR ID cannot be edited](@root/images/ror-blog-post-wcc-nielsen-05.png)

“Oh good, someone has already put it in.”

</div>

{%- endcall %}
{% call slide_grid_even_split() %}

## Users are shown other info they may recognize

![Heuristic 6: Recognition rather than recall. Minimize the user's memory load by making elements, actions, and options visible. Avoid making users remember information.](@root/images/nielsens-ten-06-with-example.png)

<div class="flow">

![The Janeway ROR search showing the information presented for recognition](@root/images/ror-blog-post-wcc-nielsen-06.png)

“Ah yes, that's the WCC I know.”

</div>

{%- endcall %}
{% call slide_text() %}

## Users can put ROR ID in Janeway using ORCID

![The Janeway login screen with an option to use ORCID](@root/images/ror-blog-post-login-orcid.png)

![The Janeway profile page showing a ROR affiliation that was populated from ORCID data](@root/images/ror-affiliation-profile.png)

“It looks like it got my affiliation info from my ORCID profile.”

{%- endcall %}
{% call slide_text() -%}

## URIs combine to create linked open data

We can get ROR IDs programmatically from ORCID because they encode them as URIs, creating **linked open data**.

1. User registers with ORCID
2. Janeway checks their public ORCID profile for affiliations
3. Janeway imports the primary affiliation and matches any ROR URI with other ROR data in the Janeway database
4. Janeway shows the post-login screen to the user

![A colourful abstract network graph of data in Wikidata](@root/images/wikidata-in-the-linked-open-data-cloud-2020-08-20-cropped.png)

{%- endcall %}
{% call slide_grid_even_split() -%}

## Users expect us to talk to other systems

![Heuristic 4: Consistency and standards. Users should not have to wonder whether different words, situations, or actions mean the same thing. Follow platform conventions.](@root/images/nielsens-ten-04-with-example.png)

<div class="flow">

![The ORCID window for adding employment](@root/images/orcid-add-employment.png)

“I have already entered my affiliation on ORCID and made it public. Can you just use that?”

</div>

{%- endcall %}
{% call slide_grid_even_split() -%}

## Users may want to edit or delete the affiliation

![Heuristic 3: User control and freedom. Users often perform actions by mistake. They need a clearly marked "emergency exit" to leave the unwanted action.](@root/images/nielsens-ten-03-with-example.png)

<div class="flow">

![The Janeway window for editing an affiliation](@root/images/ror-blog-post-edit-affiliation.png)

“Ope. My affiliation on ORCID was out of date. Let me just change that.”

</div>

{%- endcall %}
{% call slide_focus() %}

## Comparison to ORCID IDs and DOIs

{%- endcall %}
{% call slide_grid_even_split() -%}

## Turning to ORCID IDs

<div class="flow">

People’s names overlap and vary in form, just like organization names.

Real examples from orcid.org:

<div class="fs-3">

| First name | Last name |
| ---------- | --------- |
| Joseph     | Muller    |
| Joseph     | Muller    |
| Joseph     | Muller    |
| Joseph     | Muller    |
| Joseph     | Muller    |

</div>
</div>
<div class="flow">

![The ORCID logo](@root/images/orcid-logo.svg)

Should use a search interface, like with ROR records?

A search interface to choose an ORCID is not always enough. It is better to have each ORCID holder authorize the link by logging in to ORCID.

</div>

{%- endcall %}
{% call slide_grid_even_split() -%}

## Users can log in with ORCID

<div class="flow">

![The Janeway login screen with an option to use ORCID](@root/images/ror-blog-post-login-orcid.png)

![The ORCID sign-in page](@root/images/orcid-sign-in-page.png)

“Yes please. One fewer password to track.”

</div>
<div class="flow">

![Heuristic 2: Match between the system and the real world.](@root/images/nielsens-ten-02.png)

![Heuristic 4: Consistency and standards.](@root/images/nielsens-ten-04.png)

![Heuristic 6: Recognition rather than recall.](@root/images/nielsens-ten-06.png)

</div>

{%- endcall %}
{% call slide_grid_even_split() -%}

## Oh dear! ORCID IDs can be saved in various ways

<div class="flow">

Here are some real ORCID ID field values for published OLH articles:

<div class="fs-3">

| ORCID ID                               |
| -------------------------------------- |
| 0000-0002-2911-8382                    |
| https://orcid.org/0000-0002-9651-3315  |
| orcid.org/0000-0001-9039-2201          |
| https://orcid.org/ 0000-0001-8731-9097 |
| ORCID: 0000-0002-1148-689X             |
| 000-0002-8489-4405                     |
| 0009-0002-9526- 9012                   |
| nasukawa                               |

</div>
</div>
<div class="flow">

Anything can be entered into the ORCID ID field, with no required format.

![The ORCID field in Janeway](@root/images/orcid-edit-old.png)

One result: Janeway might not know which ORCID ID format to check for, letting you create a duplicate account.

(Lest you get too worried: Janeway does makes ORCID IDs uniform in outputs.)

</div>

{%- endcall %}
{% call slide_text() -%}

## Users never enter ORCID ID manually

Work in progress by Esther Verreau and Alainna Wrigley at CDL:

![The new ORCID field in Janeway](@root/images/orcid-edit-connect-your-orcid.png)

This small button will make a big difference to users and improve the quality of ORCID metadata.

<div class="flex row">

![Heuristic 4: Consistency and standards.](@root/images/nielsens-ten-04.png)

![Heuristic 5: Error prevention.](@root/images/nielsens-ten-05.png)

![Heuristic 6: Recognition rather than recall.](@root/images/nielsens-ten-06.png)

</div>

{%- endcall %}
{% call slide_grid_even_split() -%}

## Turning to DOIs

<div class="flow">

Article titles vary and overlap too, so the five whys are similar for DOIs too.

Real examples from Crossref:

<div class="fs-3">

| Title                                     |
| ----------------------------------------- |
| Back to the Future                        |
| Back to the Future                        |
| Back to the Future?                       |
| Back from the Future                      |
| Taking back the Future                    |
| Back to the Future II comment             |
| The Future Is Back; Back to the Future!\* |

</div>
</div>
<div class="flow">

![The DOI Foundation logo](@root/images/doi-foundation.svg)

Differences in circumstances:

- Generation and registration of the URI rather than retrieval and linking
- Journal editors and press managers, not authors
- Additional namespace in URI path (e.g. 10.1234)
- Multiple registation agencies
- Location matters just as much as identity since a DOI represents a digital resource

</div>

{%- endcall %}
{% call slide_grid_even_split() -%}

## Oh dear! Invalid DOIs can be created

<div class="flow">

Here are some real DOI field values for articles published on Janeway installations:

<div class="fs-3">

| DOI               |
| ----------------- |
| 10.5334/gjgl.1610 |
| 10.16995/la.9419  |
| 10.16995/la.9419  |
| /pn.2005          |
| /ahac.9516        |
| /cpo.1879         |

</div>
</div>
<div>

- Problems with uniformity and

- The middle ones are duplicates. This can lead to problems when registering the DOI, though only one is displayed on the public article page.

- The last few are missing a DOI prefix (e.g. 10.16995) so won't resolve properly.

</div>
</div>

{%- endcall %}
{% call slide_text() -%}

## Users can check resolution before publishing

<div class="grid grid-cols-2">

![A screenshot of the verify DOI tool in Janeway](@root/images/janeway-verify-doi.png)

![A screenshot of the DOI resolution status card in Janeway](@root/images/janeway-doi-resolution-status.png)

</div>

To resolve, a DOI must be:

- A valid URL
- Registered with doi.org via Crossref or Datacite
- Pointing back at the article page on Janeway

{%- endcall %}
{% call slide_text() -%}

## Users can see how the DOI resolves and catch errors

This brings in two more usability heuristics:

<div class="grid grid-cols-2">

![Heuristic 1: Visibility of system status. Designs should keep users informed about what is going on, through appropriate, timely feedback.](@root/images/nielsens-ten-01-with-example.png)

![Heuristic 9: Recognize, diagnose, and recover from errors. Error messages should be expressed in plain language (no error codes), precisely indicate the problem, and constructively suggest a solution.](@root/images/nielsens-ten-09-with-example.png)

</div>

{%- endcall %}
{% call slide_text() -%}

## What if: Users can check DOI validity earlier

We could add checks based on the expected character sequence of a DOI (using regular expressions).

These checks would happen before any communication with Crossref or Datacite, when the user...

- edits the DOI prefix and pattern fields
- advances an article, triggering a deposit
- manually creates or edits a DOI

<div class="flex">

![Heuristic 1: Visibility of system status.](@root/images/nielsens-ten-01.png)

![Heuristic 5: Error prevention.](@root/images/nielsens-ten-05.png)

</div>

{%- endcall %}
{% call slide_focus() -%}

## Takeaways

{%- endcall %}
{% call slide_text() -%}

## Takeaways

- When dealing with URIs, users work better when they have tailored interfaces that minimize error
- Top strategies for guiding users with URIs include:
  - context-rich search
  - sensible limits on what can be edited
  - input validation
  - prepopulation from linked open data
- Usability can have an affect on metadata quality
- Janeway already provides many tailored interfaces, but we need a few more for ORCID IDs and DOIs, as well as any other URIs we integrate in the future

{%- endcall %}
{% call slide_focus() -%}

## Thank you

{%- endcall %}
{% call slide_text() -%}

## References (1 of 2)

Furnas, G., T. Landauer, L. Gomez, and S. Dumais. “The Vocabulary Problem in Human-System Communication.” Communications of the ACM 30, no. 11 (1987): 964–71. https://doi.org/10.1145/32206.32212.

“Manuscript Submission Systems Integration Best Practices.” ORCID, n.d. Accessed May 18, 2026. https://info.orcid.org/manuscript-submission-systems/.

Molich, Rolf, and Jakob Nielsen. “Improving a Human-Computer Dialogue.” Communications of the ACM 33, no. 3 (1990): 338–48. https://doi.org/10.1145/77481.77486.

Muller, Joseph. From User Stories to High-Quality Data: Implementing ROR on the Janeway Platform. March 17, 2026. Text/html. https://doi.org/10.71938/E3FB-V153.

Nielsen Norman Group. “10 Usability Heuristics for User Interface Design.” Accessed May 18, 2026. https://www.nngroup.com/articles/ten-usability-heuristics/.

{%- endcall %}
{% call slide_text() -%}

## References (2 of 2)

Research Organization Registry (ROR). “About ROR.” Accessed May 18, 2026. https://ror.org/about/.

Webb, Nick. Tim Berners-Lee’s Tweet “This Is for Everyone” at the 2012 Summer Olympics Opening Ceremony. July 27, 2012. Flickr: DSC_3232. https://commons.wikimedia.org/wiki/File:This_is_for_Everyone.jpg.

{%- endcall %}
