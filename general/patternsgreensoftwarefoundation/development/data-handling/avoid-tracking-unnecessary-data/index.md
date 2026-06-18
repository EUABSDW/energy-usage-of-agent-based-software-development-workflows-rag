# https://patterns.greensoftware.foundation/development/data-handling/avoid-tracking-unnecessary-data

[Skip to main content](https://patterns.greensoftware.foundation/development/data-handling/avoid-tracking-unnecessary-data/#__docusaurus_skipToContent_fallback)

✨ We've redesigned the Green Software Patterns catalogue. Browse by [Software Lifecycle](https://patterns.greensoftware.foundation/architecture) or explore patterns for [your role](https://patterns.greensoftware.foundation/personas).

On this page

## Description [​](https://patterns.greensoftware.foundation/development/data-handling/avoid-tracking-unnecessary-data/\#description "Direct link to Description")

User tracking, user data collection and targeting in things like advertisements are responsible for significant energy use in many digital products, and services. This is primarily due to the large size of tracking and advertising scripts, the energy required to process and track user behavior, and databases collecting vast amounts of user data. Furthermore, this can present a significant violation of user privacy and tangibly degrade user experience.

## Solution [​](https://patterns.greensoftware.foundation/development/data-handling/avoid-tracking-unnecessary-data/\#solution "Direct link to Solution")

From an energy efficiency perspective, avoiding tracking unnecessary user data will reduce the overall workload for page loads and decrease overall page weight of the site.

## SCI Impact [​](https://patterns.greensoftware.foundation/development/data-handling/avoid-tracking-unnecessary-data/\#sci-impact "Direct link to SCI Impact")

`SCI = (E * I) + M per R`

[Software Carbon Intensity Spec](https://grnsft.org/sci)

Avoiding tracking unnecessary data will impact SCI as follows:

`E`: Avoiding the tracking of unnecessary data will reduce time spent on transfering and processing web pages.
`I`: Avoiding the tracking of unnecessary data will reduce the amount of energy consumed by the users browser, reducing the intensity of carbon emissions.

## Assumptions [​](https://patterns.greensoftware.foundation/development/data-handling/avoid-tracking-unnecessary-data/\#assumptions "Direct link to Assumptions")

- The term `unnecessary` here is assumed to mean data that is not required for the functionality of the site. Things like advertisements, user location, or click patterns are considered not-critical functionality for a site.

## Considerations [​](https://patterns.greensoftware.foundation/development/data-handling/avoid-tracking-unnecessary-data/\#considerations "Direct link to Considerations")

- Consider what data is absolutely critical to your site functionality and what data can be deferred, sampled, or aggregated from other more energy efficient sources.

## References [​](https://patterns.greensoftware.foundation/development/data-handling/avoid-tracking-unnecessary-data/\#references "Direct link to References")

- [https://github.com/Green-Software-Foundation/green-software-patterns/issues/52](https://github.com/Green-Software-Foundation/green-software-patterns/issues/52)
- [Does the website avoid tracking user behavior and collecting data unnecessarily?](https://sustainablewebdesign.org/does-the-website-avoid-tracking-user-behaviour-and-collecting-data-unnecessarily/)

- [Description](https://patterns.greensoftware.foundation/development/data-handling/avoid-tracking-unnecessary-data/#description)
- [Solution](https://patterns.greensoftware.foundation/development/data-handling/avoid-tracking-unnecessary-data/#solution)
- [SCI Impact](https://patterns.greensoftware.foundation/development/data-handling/avoid-tracking-unnecessary-data/#sci-impact)
- [Assumptions](https://patterns.greensoftware.foundation/development/data-handling/avoid-tracking-unnecessary-data/#assumptions)
- [Considerations](https://patterns.greensoftware.foundation/development/data-handling/avoid-tracking-unnecessary-data/#considerations)
- [References](https://patterns.greensoftware.foundation/development/data-handling/avoid-tracking-unnecessary-data/#references)