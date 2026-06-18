# https://patterns.greensoftware.foundation/development/media-and-code-efficiency/use-compiled-languages

[Skip to main content](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/use-compiled-languages/#__docusaurus_skipToContent_fallback)

✨ We've redesigned the Green Software Patterns catalogue. Browse by [Software Lifecycle](https://patterns.greensoftware.foundation/architecture) or explore patterns for [your role](https://patterns.greensoftware.foundation/personas).

On this page

## Description [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/use-compiled-languages/\#description "Direct link to Description")

Interpreted languages need to be parsed, compiled and executed when the application starts or a workload arrives. This tends to be more energy heavy then when a compiled language is used. The compilation is then only done once, saving on resources.

## Solution [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/use-compiled-languages/\#solution "Direct link to Solution")

Use compiled languages (like Go, Rust, Java or others) whenever possible or compile interpreted languages.

## SCI Impact [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/use-compiled-languages/\#sci-impact "Direct link to SCI Impact")

`SCI = (E * I) + M per R`

[Software Carbon Intensity Spec](https://grnsft.org/sci)

Concerning the SCI equation, use compiled languages will impact as follows:

- `E`: Running compiled binaries is more energy efficient and uses less energy which outweighs the energy consumed in compiling it to binary upfront
- `M`: The embodied carbon emissions will be reduced, as compiled binaries tend to be smaller then the sources they are compiled from

## Assumptions [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/use-compiled-languages/\#assumptions "Direct link to Assumptions")

- There is the assumption that the execution environment allows usage of compiled languages, this is not always the case (for example web browsers)
- Use benchmarks to determine if the application use case benefits from using a compiled language.

## Considerations [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/use-compiled-languages/\#considerations "Direct link to Considerations")

- Some interpreted languages provide ways to be compiled into binary (for example GraalVM for Java, Python and more)
- Consider factoring in compile time when doing benchmarks

## References [​](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/use-compiled-languages/\#references "Direct link to References")

- [One Carbon intensity benchmark](https://greenlab.di.uminho.pt/wp-content/uploads/2017/10/sleFinal.pdf)

- [Description](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/use-compiled-languages/#description)
- [Solution](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/use-compiled-languages/#solution)
- [SCI Impact](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/use-compiled-languages/#sci-impact)
- [Assumptions](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/use-compiled-languages/#assumptions)
- [Considerations](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/use-compiled-languages/#considerations)
- [References](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/use-compiled-languages/#references)