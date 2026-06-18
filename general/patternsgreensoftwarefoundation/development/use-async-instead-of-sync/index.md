# https://patterns.greensoftware.foundation/development/use-async-instead-of-sync

[Skip to main content](https://patterns.greensoftware.foundation/development/use-async-instead-of-sync/#__docusaurus_skipToContent_fallback)

✨ We've redesigned the Green Software Patterns catalogue. Browse by [Software Lifecycle](https://patterns.greensoftware.foundation/architecture) or explore patterns for [your role](https://patterns.greensoftware.foundation/personas).

On this page

## Description [​](https://patterns.greensoftware.foundation/development/use-async-instead-of-sync/\#description "Direct link to Description")

When making calls across process boundaries to either databases or file systems or REST APIs, relying on synchronous calls can cause the calling thread to become blocked, putting additional load on the CPU.

## Solution [​](https://patterns.greensoftware.foundation/development/use-async-instead-of-sync/\#solution "Direct link to Solution")

Using asynchronous patterns frees the calling thread from being blocked on the response and, as such, additional work can be achieved without CPU cycles being consumed.

## SCI Impact [​](https://patterns.greensoftware.foundation/development/use-async-instead-of-sync/\#sci-impact "Direct link to SCI Impact")

`SCI = (E * I) + M per R`

[Software Carbon Intensity Spec](https://grnsft.org/sci)

Using asyncronous calling patterns impacts SCI as follows:

- `E`: Optimal utilization of the CPU leads to reduced energy consumption
- `M`: Optimized average CPU utilization can reduce the amount of resources needed which will decrease the amount of embodied carbon required to support them

## Assumptions [​](https://patterns.greensoftware.foundation/development/use-async-instead-of-sync/\#assumptions "Direct link to Assumptions")

- The specific library for making asynchronous calls is available in the language being used for web development e.g. Task parallel library in C#.

## Considerations [​](https://patterns.greensoftware.foundation/development/use-async-instead-of-sync/\#considerations "Direct link to Considerations")

- Consider higher level patterns for asynchronous communication as well e.g. Queues, Topics and Streams

## References [​](https://patterns.greensoftware.foundation/development/use-async-instead-of-sync/\#references "Direct link to References")

- Async/Await ( [https://en.wikipedia.org/wiki/Async/await](https://en.wikipedia.org/wiki/Async/await))
- [Azure Well-Architected Framework Sustainability Pillar](https://learn.microsoft.com/en-us/azure/architecture/framework/sustainability/sustainability-application-design)

- [Description](https://patterns.greensoftware.foundation/development/use-async-instead-of-sync/#description)
- [Solution](https://patterns.greensoftware.foundation/development/use-async-instead-of-sync/#solution)
- [SCI Impact](https://patterns.greensoftware.foundation/development/use-async-instead-of-sync/#sci-impact)
- [Assumptions](https://patterns.greensoftware.foundation/development/use-async-instead-of-sync/#assumptions)
- [Considerations](https://patterns.greensoftware.foundation/development/use-async-instead-of-sync/#considerations)
- [References](https://patterns.greensoftware.foundation/development/use-async-instead-of-sync/#references)