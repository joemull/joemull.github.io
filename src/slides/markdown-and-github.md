---
title: Markdown and GitHub
date: 2025-10-07
type: slide_deck
---

{% from "slide_components/slide_columns.jinja" import slide_columns %}
{% from "slide_components/slide_frame.jinja" import slide_frame %}
{% from "slide_components/slide_grid_four_images.jinja" import slide_grid_four_images %}
{% from "slide_components/slide_render_markup.jinja" import slide_render_markup %}
{% from "slide_components/slide_text.jinja" import slide_text %}
{% from "slide_components/slide_video.jinja" import slide_video %}
{% from "slide_components/slide_quote.jinja" import slide_quote %}

{% call slide_render_markup(input_heading="Input") -%}

## Why do computers need markup?

Jury acquits attorney of tax fraud charges Oliver Laughland and Ramon Antonio Vargas in New Orleans Thu 28 Jul 2022 18.12 EDT New Orleans’s district attorney, Jason Williams, has been acquitted of all charges... Williams, along with his private practice law partner Nicole Burdett, faced a 10-count federal indictment...

{% endcall %}

{% call slide_render_markup(input_heading="Input", language="plain text") -%}

## Spaces and symbols express the structure

# Jury acquits attorney of tax fraud charges

_Oliver Laughland and Ramon Antonio Vargas in New Orleans_

**Thu 28 Jul 2022** 18.12 EDT

New Orleans’s district attorney, Jason Williams, has been acquitted of all charges...

Williams, along with his private practice law partner Nicole Burdett, faced a 10-count federal indictment...

{% endcall %}

{% call slide_grid_four_images() -%}

## What kind of markup is best? (Coombs 1987, 936)

![An example of no markup, not even spaces and punctuation](@root/images/no-markup.png)
![An example of presentational markup, with white space around a block quote](@root/images/presentational-markup.png)
![An example of procedural markup, with detailed code for a printer or typesetting application](@root/images/procedural-markup.png)
![An example of descriptive markup, with a semantic tag opening the block quote and closing it](@root/images/descriptive-markup.png)

{%- endcall %}

{% call slide_quote(citation="Coombs 1987, 937", url="https://doi.org/10.1145/32206.32209") -%}

“Presentational markup is designed for reading. Procedural markup is designed for formatting, but usually only by a single program. Descriptive markup is moderately well suited for reading, but primarily designed to support an open class of applications (e.g., information retrieval).”

{%- endcall %}

{% call slide_text() -%}

## Descriptive markup advantages

Coombs and his coauthors identified four advantages of **descriptive** markup (1987, 946):

1. Simpler authoring process because focus is just on content
   - Declarative over procedural programming
   - Separation of form and content
2. Easier maintenance over time
   - Abstraction of typesetting behavior away from authoring context
3. More portability once standardised
   - The World Wide Web would be created in another 10 years
4. Semantic and pragmatic information allow for alternative views
   - Semantic markup is the foundation of accessible web content

{%- endcall %}

{% call slide_video(
  "“What is Markdown?” by Code Academy on YouTube",
  "https://www.youtube.com/watch?v=f49LJV1i-_w",
  "https://img.youtube.com/vi/f49LJV1i-_w/maxresdefault.jpg"
) -%}

## Watch: What is Markdown?

{%- endcall %}

{% call slide_text() -%}

## Live coding: Examples of Markdown

You can experiment with Markdown using any environment that supports it as an authoring format.

Some examples:

- Garen Torikian, [Markdown Tutorial](https://www.markdowntutorial.com/)
- [The README.md file for the Web Development repository on GitHub](https://github.com/Birkbeck2/web-development/blob/main/README.md)
- Your code editor, if you already use one, with a markdown plugin or extension

{%- endcall %}

{% call slide_video(
  "“What is GitHub?” by Brian O’Grady on YouTube",
  "https://youtu.be/BUE2LaSzijM",
  "https://img.youtube.com/vi/BUE2LaSzijM/maxresdefault.jpg"
) -%}

## Watch: What is GitHub?

{%- endcall %}

{% call slide_text() -%}

## GitHub repository examples

GitHub repositories can be anything from major commercial software projects to small personal experiments.

| Repository                                                              | Description                                                        |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------ |
| [vuejs/core](https://github.com/vuejs/core)                             | a large free and open source (FOSS) JavaScript framework           |
| [openlibhums/janeway](https://github.com/openlibhums/janeway)           | a FOSS web application with a handful of developers, including Joe |
| [openlibhums/memory-alpha](https://github.com/openlibhums/memory-alpha) | a user support website under construction, currently private       |
| [avauga03/DietRight](https://github.com/avauga03/DietRight/)            | a student website with a nutrition theme                           |

{%- endcall %}

{% call slide_text() -%}

## Things to notice on a GitHub repository

- The owner (can be a person or organization)
- The code file structure
- The README file
- Documentation of current development in issues and pull requests
- Ability to view any code file and see who wrote each line, and when
- Number, frequency, and date of commits and releases
- Public vs. private visibility, open source licenses
- Number of contributors
- Number of forks and stars
- Breakdown of languages

{%- endcall %}

{% call slide_quote(citation="Santos 2023, 9", url="https://doi.org/10.1109/ICSE-SEIS58686.2023.00007") -%}

"In our study, we investigated to what extent the GitHub interface embedded inclusivity bugs and how these inclusivity bugs impacted users’ performance with different cognitive styles (i.e., Abis and Tims)... Participants in the Control group felt scared by the GitHub interface; (3) process-oriented learners were hampered by a lack of clear instructions on how to contribute."

{%- endcall %}

{% call slide_frame() -%}

## References

Codecademy. _What Is Markdown?_ 2019, https://www.youtube.com/watch?v=f49LJV1i-_w.

Code Institute. 2022. _What Is GitHub | How to Use It | Benefits of GitHub._ https://www.youtube.com/watch?v=BUE2LaSzijM.

Coombs, James H., Allen H. Renear, and Steven J. DeRose. 1987. “Markup Systems and the Future of Scholarly Text Processing.” _Communications of the ACM_ 30 (11): 933–47. https://doi.org/10.1145/32206.32209.

Santos, Italo, João Felipe Pimentel, Igor Wiese, Igor Steinmacher, Anita Sarma, and Marco A. Gerosa. 2023. “Designing for Cognitive Diversity: Improving the GitHub Experience for Newcomers.” _2023 IEEE/ACM 45th International Conference on Software Engineering: Software Engineering in Society (ICSE-SEIS)_, May, 1–12. https://doi.org/10.1109/ICSE-SEIS58686.2023.00007.

Torikian, Garen. n.d. “Markdown Tutorial.” Accessed October 5, 2025. https://www.markdowntutorial.com/.

{%- endcall %}
