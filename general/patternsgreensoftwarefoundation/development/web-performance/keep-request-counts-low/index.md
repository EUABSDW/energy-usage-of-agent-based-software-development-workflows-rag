# https://patterns.greensoftware.foundation/development/web-performance/keep-request-counts-low

[Skip to main content](https://patterns.greensoftware.foundation/development/web-performance/keep-request-counts-low/#__docusaurus_skipToContent_fallback)

✨ We've redesigned the Green Software Patterns catalogue. Browse by [Software Lifecycle](https://patterns.greensoftware.foundation/architecture) or explore patterns for [your role](https://patterns.greensoftware.foundation/personas).

On this page

## Description [​](https://patterns.greensoftware.foundation/development/web-performance/keep-request-counts-low/\#description "Direct link to Description")

Accessing a web page usually retrieves a HTML file from the web server. The HTML may then reference additional resources that the browser has to download. More requests means more energy consumed. As such, reducing the amount of files needed to display a page in the browser also reduces the environmental impact.

## Solution [​](https://patterns.greensoftware.foundation/development/web-performance/keep-request-counts-low/\#solution "Direct link to Solution")

Reduce the amount of files needed and requests made by the loaded JavaScript in order to display the final page.

## SCI Impact [​](https://patterns.greensoftware.foundation/development/web-performance/keep-request-counts-low/\#sci-impact "Direct link to SCI Impact")

`SCI = (E * I) + M per R`

[Software Carbon Intensity Spec](https://grnsft.org/sci)

Keeping request counts low will impact SCI as follows:

- `E`: Reducing the amount of requests reduces the energy needed to display the page
- `M`: Reducing the amount of requests can also reduce the amount of files and therefore the storage requirements of the web page on the server

## Assumptions [​](https://patterns.greensoftware.foundation/development/web-performance/keep-request-counts-low/\#assumptions "Direct link to Assumptions")

## Considerations [​](https://patterns.greensoftware.foundation/development/web-performance/keep-request-counts-low/\#considerations "Direct link to Considerations")

- Consider setting up request count budgets that are measured when the application is tested via test automation

## References [​](https://patterns.greensoftware.foundation/development/web-performance/keep-request-counts-low/\#references "Direct link to References")

- [Detailed description](https://web.dev/resource-summary/)

- [Description](https://patterns.greensoftware.foundation/development/web-performance/keep-request-counts-low/#description)
- [Solution](https://patterns.greensoftware.foundation/development/web-performance/keep-request-counts-low/#solution)
- [SCI Impact](https://patterns.greensoftware.foundation/development/web-performance/keep-request-counts-low/#sci-impact)
- [Assumptions](https://patterns.greensoftware.foundation/development/web-performance/keep-request-counts-low/#assumptions)
- [Considerations](https://patterns.greensoftware.foundation/development/web-performance/keep-request-counts-low/#considerations)
- [References](https://patterns.greensoftware.foundation/development/web-performance/keep-request-counts-low/#references)