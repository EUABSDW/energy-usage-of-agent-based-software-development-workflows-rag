# https://patterns.greensoftware.foundation/development/media-and-code-efficiency/remove-unused-css

[Skip to main content](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/remove-unused-css/#__docusaurus_skipToContent_fallback)

✨ We've redesigned the Green Software Patterns catalogue. Browse by [Software Lifecycle](https://patterns.greensoftware.foundation/architecture) or explore patterns for [your role](https://patterns.greensoftware.foundation/personas).

On this page

## Description [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/remove-unused-css/\#description "Direct link to Description")

Cascading Style Sheets (CSS) allow HTML content to be styled in a very exact way. In order to have this flexibility, the CSS files are very complex and need energy intensive parsing and processing. The browser needs to download all specified CSS files, process all definitions inside these files, apply it to the DOM and calculate the layout for rendering. Each added CSS definition increases the amount of time and processing power needed in this process.

## Solution [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/remove-unused-css/\#solution "Direct link to Solution")

Remove all unused CSS definitions if they aren't used on the website at all. Also consider combining multiple CSS files into one file to reduce the amount of requests, and therefore time, the browser needs to retrieve all CSS definitions at once.

## SCI Impact [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/remove-unused-css/\#sci-impact "Direct link to SCI Impact")

`SCI = (E * I) + M per R`

[Software Carbon Intensity Spec](https://grnsft.org/sci)

Removing unused CSS definitions will impact SCI as follows:

- `E`: Reduces the processing, memory and bandwidth requirements to display the page and therefore the energy requirements.

## Assumptions [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/remove-unused-css/\#assumptions "Direct link to Assumptions")

None

## Considerations [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/remove-unused-css/\#considerations "Direct link to Considerations")

- Depending on the web page, consider crafting specialized CSS files for landing pages or highly frequented web pages. This also makes sense if a landing page has a completely different layout as the rest of the web page.

## References [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/remove-unused-css/\#references "Direct link to References")

- [Unused CSS Rules reference](https://web.dev/unused-css-rules/)

- [Description](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/remove-unused-css/#description)
- [Solution](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/remove-unused-css/#solution)
- [SCI Impact](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/remove-unused-css/#sci-impact)
- [Assumptions](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/remove-unused-css/#assumptions)
- [Considerations](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/remove-unused-css/#considerations)
- [References](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/remove-unused-css/#references)