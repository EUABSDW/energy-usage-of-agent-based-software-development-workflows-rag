# https://patterns.greensoftware.foundation/development/data-handling/compress-transmitted-data

[Skip to main content](https://patterns.greensoftware.foundation/development/data-handling/compress-transmitted-data/#__docusaurus_skipToContent_fallback)

✨ We've redesigned the Green Software Patterns catalogue. Browse by [Software Lifecycle](https://patterns.greensoftware.foundation/architecture) or explore patterns for [your role](https://patterns.greensoftware.foundation/personas).

On this page

## Description [​](https://patterns.greensoftware.foundation/development/data-handling/compress-transmitted-data/\#description "Direct link to Description")

From an energy-efficiency perspective, it's better to minimise the size of the data transmitted so that less energy is required because the network traffic is reduced.

## Solution [​](https://patterns.greensoftware.foundation/development/data-handling/compress-transmitted-data/\#solution "Direct link to Solution")

Minimise the size of data transmitted by compressing files or payloads.

## SCI Impact [​](https://patterns.greensoftware.foundation/development/data-handling/compress-transmitted-data/\#sci-impact "Direct link to SCI Impact")

`SCI = (E * I) + M per R` [Software Carbon Intensity Spec](https://grnsft.org/sci)

Reducing the distance will impact SCI as follows:

- `E`: We reduce the total electricity required by reducing network traffic. However, we should be wary that there may be a slight increase in energy consumed due to compressing and de-compressing data.
- `I`: We may also have a slight increase in location-based marginal carbon emissions due to compressing and de-compressing data at different locations.

## Assumptions [​](https://patterns.greensoftware.foundation/development/data-handling/compress-transmitted-data/\#assumptions "Direct link to Assumptions")

Suppose we choose to transfer data (e.g. files or payloads) to the client side because that is the only format the client side can handle. A better solution would be to consider a compressing mechanism for large files or payloads before sending them across the network to the client side to reduce overall network traffic.

## Considerations [​](https://patterns.greensoftware.foundation/development/data-handling/compress-transmitted-data/\#considerations "Direct link to Considerations")

- It may reduce cloud bills because minimising the size of the data transmitted will cost less.
- If a compressed asset cannot be dealt with, there is more overhead to resend the asset in the correct format.

## References [​](https://patterns.greensoftware.foundation/development/data-handling/compress-transmitted-data/\#references "Direct link to References")

- [Energy Efficiency Principle](https://learn.greensoftware.foundation/practitioner/energy-efficiency)

- [Description](https://patterns.greensoftware.foundation/development/data-handling/compress-transmitted-data/#description)
- [Solution](https://patterns.greensoftware.foundation/development/data-handling/compress-transmitted-data/#solution)
- [SCI Impact](https://patterns.greensoftware.foundation/development/data-handling/compress-transmitted-data/#sci-impact)
- [Assumptions](https://patterns.greensoftware.foundation/development/data-handling/compress-transmitted-data/#assumptions)
- [Considerations](https://patterns.greensoftware.foundation/development/data-handling/compress-transmitted-data/#considerations)
- [References](https://patterns.greensoftware.foundation/development/data-handling/compress-transmitted-data/#references)