# https://patterns.greensoftware.foundation/development/evaluate-whether-to-use-TLS-termination

[Skip to main content](https://patterns.greensoftware.foundation/development/evaluate-whether-to-use-TLS-termination/#__docusaurus_skipToContent_fallback)

✨ We've redesigned the Green Software Patterns catalogue. Browse by [Software Lifecycle](https://patterns.greensoftware.foundation/architecture) or explore patterns for [your role](https://patterns.greensoftware.foundation/personas).

On this page

## Description [​](https://patterns.greensoftware.foundation/development/evaluate-whether-to-use-TLS-termination/\#description "Direct link to Description")

Transport Layer Security (TLS) ensures that all data passed between the web server and web browsers remain private and encrypted. However, terminating and re-establishing TLS increases CPU usage and might be unnecessary in certain architectures.

## Solution [​](https://patterns.greensoftware.foundation/development/evaluate-whether-to-use-TLS-termination/\#solution "Direct link to Solution")

Terminate TLS at your border gateway and continue with non-TLS to your application load balancer and onwards to your workload.

## SCI Impact [​](https://patterns.greensoftware.foundation/development/evaluate-whether-to-use-TLS-termination/\#sci-impact "Direct link to SCI Impact")

`SCI = (E * I) + M per R` [Software Carbon Intensity Spec](https://grnsft.org/sci)

Implementing non-TLS communication will impact SCI as follows:

- `E`: By reducing CPU, the amount of energy needed to support the communication transport is reduced.
- `M`: By reducing the compute resource requirements, the total embodied carbon emissions are reduced.

## Assumptions [​](https://patterns.greensoftware.foundation/development/evaluate-whether-to-use-TLS-termination/\#assumptions "Direct link to Assumptions")

The application does not have compliance requirements for using end-to-end TLS.

## Considerations [​](https://patterns.greensoftware.foundation/development/evaluate-whether-to-use-TLS-termination/\#considerations "Direct link to Considerations")

A balanced level of security can offer a more sustainable and energy efficient workload while a higher level of security may increase the requirements on compute resources.

Consider applying the _Just Enough Security_ (JES) model and terminate TLS at your border gateway for most standard applications that do not have strict compliance requirements.

## References [​](https://patterns.greensoftware.foundation/development/evaluate-whether-to-use-TLS-termination/\#references "Direct link to References")

[Microsoft Azure Well-Architected Framework Sustainability Patterns](https://learn.microsoft.com/en-us/azure/architecture/framework/sustainability/sustainability-security)

- [Description](https://patterns.greensoftware.foundation/development/evaluate-whether-to-use-TLS-termination/#description)
- [Solution](https://patterns.greensoftware.foundation/development/evaluate-whether-to-use-TLS-termination/#solution)
- [SCI Impact](https://patterns.greensoftware.foundation/development/evaluate-whether-to-use-TLS-termination/#sci-impact)
- [Assumptions](https://patterns.greensoftware.foundation/development/evaluate-whether-to-use-TLS-termination/#assumptions)
- [Considerations](https://patterns.greensoftware.foundation/development/evaluate-whether-to-use-TLS-termination/#considerations)
- [References](https://patterns.greensoftware.foundation/development/evaluate-whether-to-use-TLS-termination/#references)