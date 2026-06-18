# https://patterns.greensoftware.foundation/development/media-and-code-efficiency/defer-offscreen-images

[Skip to main content](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/defer-offscreen-images/#__docusaurus_skipToContent_fallback)

✨ We've redesigned the Green Software Patterns catalogue. Browse by [Software Lifecycle](https://patterns.greensoftware.foundation/architecture) or explore patterns for [your role](https://patterns.greensoftware.foundation/personas).

On this page

## Description [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/defer-offscreen-images/\#description "Direct link to Description")

Web pages offer a lot of images that aren't displayed on the first loaded screen. They can also hide these images behind other interactions, like tabs and accordions. This content is dynamically displayed and therefore doesn't need to be loaded when it isn't displayed.

The fact that images are loaded on-demand, only when they are about to be displayed, is often called "lazy-loading".

## Solution [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/defer-offscreen-images/\#solution "Direct link to Solution")

Use on demand loading for images which are unlikely to be displayed on first page load. This can be done via the newer browser attribute `loading="lazy"` on the image tag and can also be [polyfilled](https://github.com/mfranzke/loading-attribute-polyfill) for older browsers.

## SCI Impact [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/defer-offscreen-images/\#sci-impact "Direct link to SCI Impact")

`SCI = (E * I) + M per R`

[Software Carbon Intensity Spec](https://grnsft.org/sci)

Using lazy loading of images will impact SCI as follows:

- `E`: Images are only loaded when needed, saving bandwidth and processing power on the client and server, therefore reducing the energy required.

## Assumptions [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/defer-offscreen-images/\#assumptions "Direct link to Assumptions")

- This assumes that the HTML for the image tags can be modified in the application

## Considerations [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/defer-offscreen-images/\#considerations "Direct link to Considerations")

None

## References [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/defer-offscreen-images/\#references "Direct link to References")

- [Detailed description](https://web.dev/offscreen-images/)

- [Description](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/defer-offscreen-images/#description)
- [Solution](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/defer-offscreen-images/#solution)
- [SCI Impact](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/defer-offscreen-images/#sci-impact)
- [Assumptions](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/defer-offscreen-images/#assumptions)
- [Considerations](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/defer-offscreen-images/#considerations)
- [References](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/defer-offscreen-images/#references)