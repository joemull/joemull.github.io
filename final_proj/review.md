# Accessibility Review of Michigan Publishing Website
View the website at [publishing.umich.edu](https://www.publishing.umich.edu)

# Issues
We used the POUR framework from the WCAG 2.1 AA standard to group the issues we found. We listed cases for which these situations affect accessibility.

## Perceivable

### Color contrast
__There are contrast issues with color used to link words and with the yellow quotation marks.__

![Blue text color contrast](https://joemull.github.io/final_proj/screenshots/1e80a2.png)

![Gray text color contrast](https://joemull.github.io/final_proj/screenshots/8a96a1.png)

![Gray text color contrast](https://joemull.github.io/final_proj/screenshots/b4b4b5.png)

![Yellow text color contrast](https://joemull.github.io/final_proj/screenshots/ffcb05.png)

 - __Location__: All pages with linked text and yellow quotation marks
 - __Use Case__: Someone who has low vision needs higher contrast between foreground and background colors. Also, anyone who is visiting the website outside on a bright day may not be able to read text with low contrast.

__The map markers don't contrast enough with the gray map background.__

![Yellow text color contrast](https://joemull.github.io/final_proj/screenshots/map-markers.png)

- __Location__: "Our Reach" page
- __Use Case__: Same as above.

### Alternative text
__Alt text is missing in places with certain image__

![Alt text on Stories page](https://joemull.github.io/final_proj/screenshots/stories-alt.png)
- __Location__: Thumbnails on the "Stories of Impact" landing page
- __Use Case__: Those with vision impairments who use screen readers need alt text to understand the context of images on the page.

__Alt text could be improved in places.__ redundant with other text near the image, and it should not start with "a photo of" or "an image of."

![Redundant alt text](https://joemull.github.io/final_proj/screenshots/redundant-alt.png)

![Alt text with "A photo of"](https://joemull.github.io/final_proj/screenshots/wordy-alt.png)
- __Location__: All places where images are present
- __Use Case__: Those who use screen readers would hear this information read twice, once for the image and once for the on-screen text. Screen reader users will also usually know that something is an image, so "an image of" is not necessary.

__Best practices are not always followed for decorative images.__

![Empty alt not used](https://joemull.github.io/final_proj/screenshots/button-alt-empty.png)

- __Location__: Zoom buttons on maps on "Our Reach."ARIA role `presentation` may not be best for decorative images that have alt text.__

![ARIA on img](https://joemull.github.io/final_proj/screenshots/aria-img.png)
- __Location__: Trending section of main page.
- __Use Case__:  Users of screen readers will depend on their technology detecting the right semantic role of decorative images. All decorative images should have empty alt text, or if another strategy is used, only one strategy should be used consistently, and there are now better supported ways for doing that here.

### Text size

__Text size is too small in certain places.__

![Search bar](https://joemull.github.io/final_proj/screenshots/search-bar.png)
- __Location__: "Search" page
- __Use Case__: Those with visual impairments need a larger text size to be able to read the page.

__Text zooming makes elements hard to read.__

![Zoom text only](https://joemull.github.io/final_proj/screenshots/zoom-text-only.png)
- __Location__: Navigation bar of all pages

![Zoom text only - numbers](https://joemull.github.io/final_proj/screenshots/zoom-text-only-numbers.png)
- __Location__: "By the numbers" on the home page

![Zoom text only - map](https://joemull.github.io/final_proj/screenshots/zoom-text-only-map-filter.png)
- __Location__: Second map on "Our Reach"

![Zoom text only - map](https://joemull.github.io/final_proj/screenshots/zoom-text-only-social.png)
- __Location__: Footer on "all pages"
- __Use Case__: Some users expand just the text size in their browser, and if this causes text fields to run over or run together, the user cannot read easily.  


### Semantic HTML elements

__Layout using `table` HTML element is misleading.__

![Table for search bar](https://joemull.github.io/final_proj/screenshots/search-table.png)
- __Location__: "Search" page "Custom Google Search" bar
- __Use Case__: Those using screen readers can be confused by the layout `table` HTML element, as it exists just for content that needs formatting as tabular data.

## Operable

### Semantic HTML elements

__Some headers and headings are empty.__

![Emptymt html headings](https://joemull.github.io/final_proj/screenshots/empty-h2s.png)
- __Location__: "Mission" page, in the space just before the footer
- __Use Case__: Those who use screen readers or navigate by keyboard often use headers and headings to orient themselves on the page. These elements need to include text so that a user can move throughout the page with context.

__Some headers are inside other headers or not distinguished from each other__.

![Header in header](https://joemull.github.io/final_proj/screenshots/header-in-header.png)

- __Location__: The persistent header on all pages.

![Empty html header](https://joemull.github.io/final_proj/screenshots/empty-header-iframe.png)
- __Location__: "Our Reach" page, inside the `iframe` for the first map.
- __Use Case__: Users of screen readers depend on semantic HTML elements to navigate, and nested header el may not let them do so without difficulty.

__There are some gaps in heading levels.__

![Empty heading gap](https://joemull.github.io/final_proj/screenshots/h1-h3.png)
- __Location__: "Stories of Impact" page
- __Use Case__: Users of screen readers depend on headings to navigate, so they should only occur in order from `h1` to `h6`.

### Landmarks
__ARIA labels are missing where they are needed due to iframes.__

- __Location__: The `header`, `main` and `footer` elements of most pages
- __Use Case__: When screen readers encounter pages that have iframe, they sometimes depend on ARIA labels to tell important but duplicated HTML tags like `header`, `main`, and `footer` apart and identify landmarks that allow users to navigate.

### Table Elements

### Videos and Images
__Autoplay on videos and animated images__

__No "height" or "width" attribute on images__

### Keyboard Accessibility
__No "Skip to Content" link provided__.

__"Onclick" events should have keyboard alternatives__.



## Understandable

### Unclear titles and labels

__Search bar has a title, but not an HTML label.__

![Form needs title](https://joemull.github.io/final_proj/screenshots/form-needs-title.png)

- __Location__: "Search" page "Custom Google Search" bar
- __Use Case__: Screen readers need a label HTML element or aria-labeledby element to correctly communicate to the user that this page has a search bar.

__The two map elements have the same title.__

![Form needs title](https://joemull.github.io/final_proj/screenshots/map-title.png)
- __Location__: Maps on "Our Reach" page
- __Use Case__: Users of screen readers won't be able to tell how the maps are different when navigating using the two titles

## Robust

__No errors found__

# Recommendations
We broke down our technical recommendations by web design role to make them easy to implement.

## Content Creator
- Edit alt text labels to be different or more descriptive than redundant on-page text
- For decorative images, use empty alt text labels `alt=""` rather than ARIA `role="presentation"`
- Generate descriptive alt text for images that don't have them
- Generate text for the empty HTML header elements, or delete them
- For decorative images, consider emptying alt text field: `alt=""`
- Generate separate titles for the two maps

## HTML / Markup
- Add adjusted alt-text labels and add created blank labels
- Remove ARIA `role="presentation"` where alt text value is empty.
- Create a different, non-tabular format for the search bar.
- Add an aria-labeledby element to the search bar.
- Add ARIA landmark labels to differentiate main `header`,`main` and `footer` from iframe elements
ements
- Change heading levels so that there aren't any gaps ("Stories of Impact")
- Change titles of maps as neededRemove or add text to the empty HTML header el- ements

## CSS / Design
- Adjust coloring contrast issues for linked text and stylized quotation marks (you can use [wave.webaim.org](https://wave.webaim.org) to determine when the color contrast is AA-approved.
- For the map markers, you have to checking contrast manually. You can get hex codes from foreground and background images in Photoshop (or by uploading them to color.adobe.com) and plug those codes into the WebAIM Contrast Checker. WCAG AA calls for a contrast of at least 3:1 for graphics. Current colors:
	- map background - #E8E8E8
	-  blue marker - #008CFF, contrast ratio of 2.76:1
	- yellow marker - #F2B705, contrast ratio of 1.48:1

- Adjust text size in noted places.
- Create styling for the search bar so that the HTML element doesn't need to be in tabular format.
- Turn off autoplay, allowing users to control when videos (or animated images longer than 5 seconds) start and stop.
- Specify width and height for images.
- Add keyboard handlers/event listeners wherever mouse ones are used.

## Resources
- [Alternative Text](https://webaim.org/techniques/alttext/)
- [How to Decide When/How to Use Alt Text](https://www.w3.org/WAI/tutorials/images/decision-tree/)
- [General Introduction to Web accessibility](https://dev.to/maxwell_dev/the-web-accessibility-introduction-i-wish-i-had-4ope)
- [Decorative Images](https://www.w3.org/WAI/tutorials/images/decorative/)
- [Banner landmark must not be contained in another landmark](https://dequeuniversity.com/rules/axe/3.3/landmark-banner-is-top-level?application=AxeChrome)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Pages must not have more than one banner landmark](https://dequeuniversity.com/rules/axe/3.3/landmark-no-duplicate-banner?application=AxeChrome)
- [Keyboard Accessibility](https://webaim.org/techniques/keyboard/)
