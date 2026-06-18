# https://patterns.greensoftware.foundation/development/minimizing-deployed-environments

[Skip to main content](https://patterns.greensoftware.foundation/development/minimizing-deployed-environments/#__docusaurus_skipToContent_fallback)

✨ We've redesigned the Green Software Patterns catalogue. Browse by [Software Lifecycle](https://patterns.greensoftware.foundation/architecture) or explore patterns for [your role](https://patterns.greensoftware.foundation/personas).

On this page

## Description [​](https://patterns.greensoftware.foundation/development/minimizing-deployed-environments/\#description "Direct link to Description")

In a given application, there may be a need to utilize multiple environments in the application workflow. Typically, a development environment is used for regular updates, while staging or testing environments are used to make sure there are no issues before code reaches a production environment where users may have access.

Each added environment has an increasing energy impact, which in turn creates more emissions. As such, it is important to understand the necessity of each environment and it's environmental impact.

## Solution [​](https://patterns.greensoftware.foundation/development/minimizing-deployed-environments/\#solution "Direct link to Solution")

From an energy-efficiency perspective, it's better to minimize the amount of deployed environments for an application so that less resources are provisioned and less energy is required.

## SCI Impact [​](https://patterns.greensoftware.foundation/development/minimizing-deployed-environments/\#sci-impact "Direct link to SCI Impact")

`SCI = (E * I) + M per R`

[Software Carbon Intensity Spec](https://grnsft.org/sci)

Reducing the amount of deployed environments will impact SCI as follows:

- `E`: We reduce the total electricity required by reducing provisioned resources.
- `M`: By reducing the amount of nodes running on underlying machines, the total embodied carbon is lower.

## Assumptions [​](https://patterns.greensoftware.foundation/development/minimizing-deployed-environments/\#assumptions "Direct link to Assumptions")

Suppose we choose to remove a deployed performance environment for an application. Another existing environment like `QA` could be repurposed for both quality assurance and performance testing to save and optimize existing resources.

## Considerations [​](https://patterns.greensoftware.foundation/development/minimizing-deployed-environments/\#considerations "Direct link to Considerations")

It may reduce cloud bills because minimising the total amount of provisioned resources will cost less. It may also create a bottleneck in the application life cycle, losing an environment created for the sole purpose of performance or QA testing.

## References [​](https://patterns.greensoftware.foundation/development/minimizing-deployed-environments/\#references "Direct link to References")

- [Energy Efficiency Principle](https://learn.greensoftware.foundation/practitioner/energy-efficiency)
- [Hardware Efficiency Principle](https://learn.greensoftware.foundation/practitioner/hardware-efficiency/)

- [Description](https://patterns.greensoftware.foundation/development/minimizing-deployed-environments/#description)
- [Solution](https://patterns.greensoftware.foundation/development/minimizing-deployed-environments/#solution)
- [SCI Impact](https://patterns.greensoftware.foundation/development/minimizing-deployed-environments/#sci-impact)
- [Assumptions](https://patterns.greensoftware.foundation/development/minimizing-deployed-environments/#assumptions)
- [Considerations](https://patterns.greensoftware.foundation/development/minimizing-deployed-environments/#considerations)
- [References](https://patterns.greensoftware.foundation/development/minimizing-deployed-environments/#references)