# https://patterns.greensoftware.foundation/development/data-handling/reduce-transmitted-data

[Skip to main content](https://patterns.greensoftware.foundation/development/data-handling/reduce-transmitted-data/#__docusaurus_skipToContent_fallback)

✨ We've redesigned the Green Software Patterns catalogue. Browse by [Software Lifecycle](https://patterns.greensoftware.foundation/architecture) or explore patterns for [your role](https://patterns.greensoftware.foundation/personas).

On this page

## Description [​](https://patterns.greensoftware.foundation/development/data-handling/reduce-transmitted-data/\#description "Direct link to Description")

From an energy-efficiency perspective, it's better to minimize the size of the data transmitted so that less energy is required because the network traffic is reduced.

## Solution [​](https://patterns.greensoftware.foundation/development/data-handling/reduce-transmitted-data/\#solution "Direct link to Solution")

Minimize the size of data transmitted by only sending properties or values deemed necessary.

## SCI Impact [​](https://patterns.greensoftware.foundation/development/data-handling/reduce-transmitted-data/\#sci-impact "Direct link to SCI Impact")

`SCI = (E * I) + M per R` [Software Carbon Intensity Spec](https://grnsft.org/sci)

Reducing the size of data will impact SCI as follows:

- `E`: We reduce the total electricity required by reducing network traffic.
- `M`: By reducing the total size of data stored, the total embodied carbon is lower.

## Assumptions [​](https://patterns.greensoftware.foundation/development/data-handling/reduce-transmitted-data/\#assumptions "Direct link to Assumptions")

- Suppose we choose to transfer data (e.g. payloads) to the client side as it is because some properties or values may be needed later. A better solution would be to consider curating the data set, ensuring only necessary properties are sent across the network so the overall network traffic is reduced. In many use cases, certain properties or values can be correlated later.

- Another consideration is that different data formats will affect the overall network traffic depending on their size. For example, Protobuf is much more compact than XML.


## Considerations [​](https://patterns.greensoftware.foundation/development/data-handling/reduce-transmitted-data/\#considerations "Direct link to Considerations")

- It may reduce cloud bills because minimising the size of the data transmitted will cost less.
- If we minimize the data set by taking away properties or values, there may be overhead to corelate the missing properties or values.

## References [​](https://patterns.greensoftware.foundation/development/data-handling/reduce-transmitted-data/\#references "Direct link to References")

- [Energy Efficiency Principle](https://learn.greensoftware.foundation/practitioner/energy-efficiency)

- [Description](https://patterns.greensoftware.foundation/development/data-handling/reduce-transmitted-data/#description)
- [Solution](https://patterns.greensoftware.foundation/development/data-handling/reduce-transmitted-data/#solution)
- [SCI Impact](https://patterns.greensoftware.foundation/development/data-handling/reduce-transmitted-data/#sci-impact)
- [Assumptions](https://patterns.greensoftware.foundation/development/data-handling/reduce-transmitted-data/#assumptions)
- [Considerations](https://patterns.greensoftware.foundation/development/data-handling/reduce-transmitted-data/#considerations)
- [References](https://patterns.greensoftware.foundation/development/data-handling/reduce-transmitted-data/#references)