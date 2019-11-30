# publishing.umich.edu

## Contrast (8)
* Element has insufficient color contrast of 4.46 (foreground color: #1e80a2, background color: #fefefe, font size: 12.0pt (16px), font weight: normal).
* Element has insufficient color contrast of 2.99 (foreground color: #8a96a1, background color: #fefefe, font size: 12.0pt (16px), font weight: normal). Expected contrast ratio of 4.5:1

## ARIA role (4)
* ARIA role `presentation` is not allowed for given element:
```html
<img src="https://books.google.com/books/content?id=sRJxDwAAQBAJ&amp;printsec=frontcover&amp;img=1&amp;zoom=2&amp;source=gbs_api" alt="Appified" role="presentation" class="trending-image overflow-hidden rounded fade-in">
```

## Banner
* The banner landmark is contained in another landmark. / Document has more than one banner landmark.
```html
<header class="border-b border-almost-black-21">
  <div class="fixed inset-0 bg-almost-black-30 z-8 hidden"></div>
  <header aria-label="View our other U-M Library sites" class="css-lveure-HeaderContainer ep434io0">
    <div class="css-nep9v8-Margins e1n9jay70">...
```

## Captions
* Captions not available for video element (map). See div `id="video-description"`.

## Audio description
* Audio description not available

# `publishing.umich.edu/our-reach`

## Contrast (17)
* Element has insufficient color contrast of 4.46 (foreground color: #1e80a2, background color: #fefefe, font size: 12.0pt (16px), font weight: normal). Expected contrast ratio of 4.5:1
* Text within Google Maps iframe
* Blue and yellow markers on second map

## Alt text (4)
* Zoom buttons

## Frame titles
* <iframe> and <frame> elements must contain a unique title attributes
```html
<iframe title="Readership map" width="100%" height="800" src="https://maps.publishing.umich.edu/readership-map/"></iframe>
```

## Landmarks
* Same doubling as `publishing.umich.edu`
* The landmark must have a unique aria-label, aria-labelledby, or title to make landmarks distinguishable
```html
<header class="border-b border-almost-black-21">
```
* The `main` class needs ARIA label to make it unique
* The footer class needs an ARIA label

## Radio button consistency
* The first radio button in the second map lacks a consistent structure as defined by ARIA

# publishing.umich.edu/our-mission

## Contrast errors
* same as above

## Empty h2s
* near footer before end of main

## Landmarks
* Same doubling

# publishing.umich.edu/stories-of-impact

## Contrast
* Element has insufficient color contrast of 2.05 (foreground color: #b4b4b5, background color: #fefefe, font size: 12.0pt (16px), font weight: bold). Expected contrast ratio of 4.5:1

## Alt Text
* Images in story hooks must have alt text

## Heading levels
* Gap in heading levels

## Landmarks
* Double headers

# publishing.umich.edu/search

## Contrast
* Same colors
* Google Custom search bar contrast

# Title
* Form needs a title

## Landmarks
* Double headers
