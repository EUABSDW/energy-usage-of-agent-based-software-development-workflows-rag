# https://patterns.greensoftware.foundation/development/data-handling/compress-stored-data

[Skip to main content](https://patterns.greensoftware.foundation/development/data-handling/compress-stored-data/#__docusaurus_skipToContent_fallback)

✨ We've redesigned the Green Software Patterns catalogue. Browse by [Software Lifecycle](https://patterns.greensoftware.foundation/architecture) or explore patterns for [your role](https://patterns.greensoftware.foundation/personas).

On this page

## Description [​](https://patterns.greensoftware.foundation/development/data-handling/compress-stored-data/\#description "Direct link to Description")

Storing too much uncompressed data can result in bandwidth waste and increase the storage capacity requirements.

## Solution [​](https://patterns.greensoftware.foundation/development/data-handling/compress-stored-data/\#solution "Direct link to Solution")

Using the right compression tool for each use case reduces the storage requirements. This includes both the capacity and required bandwidth to write or retrieve data.

## SCI Impact [​](https://patterns.greensoftware.foundation/development/data-handling/compress-stored-data/\#sci-impact "Direct link to SCI Impact")

`SCI = (E * I) + M per R`

[Software Carbon Intensity Spec](https://grnsft.org/sci)

Using compression when storing data impacts SCI as follows:

- `E`: Decreasing the amount of storage means less energy is consumed for the storage. However, compressing and de-compressing data may also cause a slight increase in energy consumed.
- `M`: Decreasing the amount of storage means there is less embodied carbon emitted.

## Assumptions [​](https://patterns.greensoftware.foundation/development/data-handling/compress-stored-data/\#assumptions "Direct link to Assumptions")

- You have the ability to choose whether you use compression or not. This is not the case if you store a lot of data, as compression is needed to keep storage costs reasonable. In the same way, if you have a limited amount of storage space, you will be forced to use a high compression (even when a high CPU is required).

## Considerations [​](https://patterns.greensoftware.foundation/development/data-handling/compress-stored-data/\#considerations "Direct link to Considerations")

- The benefit of compression should always be considered in terms of the trade-off with the increased carbon cost of the resources (e.g. CPU, RAM) needed to perform the compression/decompression.

## References [​](https://patterns.greensoftware.foundation/development/data-handling/compress-stored-data/\#references "Direct link to References")

- [Microsoft Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/sustainability/sustainability-storage#enable-storage-compression)

- [Description](https://patterns.greensoftware.foundation/development/data-handling/compress-stored-data/#description)
- [Solution](https://patterns.greensoftware.foundation/development/data-handling/compress-stored-data/#solution)
- [SCI Impact](https://patterns.greensoftware.foundation/development/data-handling/compress-stored-data/#sci-impact)
- [Assumptions](https://patterns.greensoftware.foundation/development/data-handling/compress-stored-data/#assumptions)
- [Considerations](https://patterns.greensoftware.foundation/development/data-handling/compress-stored-data/#considerations)
- [References](https://patterns.greensoftware.foundation/development/data-handling/compress-stored-data/#references)