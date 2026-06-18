# https://patterns.greensoftware.foundation/development/media-and-code-efficiency/properly-sized-images

[Skip to main content](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/properly-sized-images/#__docusaurus_skipToContent_fallback)

✨ We've redesigned the Green Software Patterns catalogue. Browse by [Software Lifecycle](https://patterns.greensoftware.foundation/architecture) or explore patterns for [your role](https://patterns.greensoftware.foundation/personas).

On this page

## Description [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/properly-sized-images/\#description "Direct link to Description")

Images are stored with fixed pixel dimensions on disk. This determines the file size and the quality that can be achieved when displaying the image on screen. Web pages let us dynamically resize the images from the stored size to a specific display size.

Ideally, the stored pixel dimensions are exactly the same, or smaller, as the display size in pixels so that no bandwidth or storage space is wasted.
The display size of images varies from device to device and can even change when the window is esized. For this use case, web browsers provide the functionality to have "responsive images". In practice, the web server stores multiple versions of the same image, then decides which image size to load depending on the screen and window size.

## Solution [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/properly-sized-images/\#solution "Direct link to Solution")

The ideal scenario is for the web browser to download the image in a size that is nearest to the display size, in order to save bandwidth and processing cost in the web browser. The generation can be done in multiple ways, for example inside the CI/CD pipeline or via a third party service (for example via Image-CDNs).

## SCI Impact [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/properly-sized-images/\#sci-impact "Direct link to SCI Impact")

`SCI = (E * I) + M per R` [Software Carbon Intensity Spec](https://grnsft.org/sci)

Optimizing the image sizes will impact SCI as follows:

- `E`: Reduces the processing and memory requirements to display the page, which also reduces the energy requirements. However, there is also an increase in the processing time for every image to convert it into the required size.
- `M`: Increases the storage requirements to cache or store all needed image sizes.

## Assumptions [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/properly-sized-images/\#assumptions "Direct link to Assumptions")

None

## Considerations [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/properly-sized-images/\#considerations "Direct link to Considerations")

- Consider using vector image formats like SVG to provide dynamically scalable images.

## References [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/properly-sized-images/\#references "Direct link to References")

- [Further explanation](https://web.dev/uses-responsive-images/)
- [Image CDNs](https://web.dev/image-cdns/)

- [Description](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/properly-sized-images/#description)
- [Solution](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/properly-sized-images/#solution)
- [SCI Impact](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/properly-sized-images/#sci-impact)
- [Assumptions](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/properly-sized-images/#assumptions)
- [Considerations](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/properly-sized-images/#considerations)
- [References](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/properly-sized-images/#references)