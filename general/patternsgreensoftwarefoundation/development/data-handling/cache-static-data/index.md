# https://patterns.greensoftware.foundation/development/data-handling/cache-static-data

[Skip to main content](https://patterns.greensoftware.foundation/development/data-handling/cache-static-data/#__docusaurus_skipToContent_fallback)

✨ We've redesigned the Green Software Patterns catalogue. Browse by [Software Lifecycle](https://patterns.greensoftware.foundation/architecture) or explore patterns for [your role](https://patterns.greensoftware.foundation/personas).

On this page

## Description [​](https://patterns.greensoftware.foundation/development/data-handling/cache-static-data/\#description "Direct link to Description")

From an energy-efficiency perspective, it's better to reduce network traffic by reading the data locally through a cache rather than accessing it remotely over the network.

Shortening the distance a network packet travels means that less energy is required to transmit it. Similarly, from an embodied carbon perspective, we are more efficient with hardware when a network packet traverses through less computing equipment.

## Solution [​](https://patterns.greensoftware.foundation/development/data-handling/cache-static-data/\#solution "Direct link to Solution")

Caching static data, such as images or audio, instead of transferring it over the network.

## SCI Impact [​](https://patterns.greensoftware.foundation/development/data-handling/cache-static-data/\#sci-impact "Direct link to SCI Impact")

`SCI = (E * I) + M per R` [Software Carbon Intensity Spec](https://grnsft.org/sci)

Reducing the distance travelled will impact SCI as follows:

- `E`: By reducing the distance a packet travels, less total electricity is required.
- `M`: By reducing the total amount of computing equipment traversed, the total embodied carbon is lower.

## Assumptions [​](https://patterns.greensoftware.foundation/development/data-handling/cache-static-data/\#assumptions "Direct link to Assumptions")

Suppose we transfer all the data of an application across the network as often as needed because some of the data may require a regular update. A better solution would be to consider a caching mechanism for static data that doesn't require frequent updates. This will reduce network traffic because we are doing local readings of the static data.

## Considerations [​](https://patterns.greensoftware.foundation/development/data-handling/cache-static-data/\#considerations "Direct link to Considerations")

- It may reduce cloud bills because shortening the path that a network packet travels will cost less.
- If data is not static anymore, there is more overhead to re-architect the application to deal with the new data requirement.
- It is assumed that a local in-memory cache of the server(s) is used to implement this pattern. If any external cache infrastructure is leveraged, then SCI score may not reduce considerably as we have to account for the E and M values of the external infrastructure in the equation.

## References [​](https://patterns.greensoftware.foundation/development/data-handling/cache-static-data/\#references "Direct link to References")

- [Hardware Efficiency Principle](https://learn.greensoftware.foundation/practitioner/hardware-efficiency)
- [Energy Efficiency Principle](https://learn.greensoftware.foundation/practitioner/energy-efficiency)

- [Description](https://patterns.greensoftware.foundation/development/data-handling/cache-static-data/#description)
- [Solution](https://patterns.greensoftware.foundation/development/data-handling/cache-static-data/#solution)
- [SCI Impact](https://patterns.greensoftware.foundation/development/data-handling/cache-static-data/#sci-impact)
- [Assumptions](https://patterns.greensoftware.foundation/development/data-handling/cache-static-data/#assumptions)
- [Considerations](https://patterns.greensoftware.foundation/development/data-handling/cache-static-data/#considerations)
- [References](https://patterns.greensoftware.foundation/development/data-handling/cache-static-data/#references)