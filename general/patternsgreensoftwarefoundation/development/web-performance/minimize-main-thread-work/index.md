# https://patterns.greensoftware.foundation/development/web-performance/minimize-main-thread-work

[Skip to main content](https://patterns.greensoftware.foundation/development/web-performance/minimize-main-thread-work/#__docusaurus_skipToContent_fallback)

✨ We've redesigned the Green Software Patterns catalogue. Browse by [Software Lifecycle](https://patterns.greensoftware.foundation/architecture) or explore patterns for [your role](https://patterns.greensoftware.foundation/personas).

On this page

## Description [​](https://patterns.greensoftware.foundation/development/web-performance/minimize-main-thread-work/\#description "Direct link to Description")

Web browsers traditionally consist of a main rendering thread that handles most of the updates on the web page and the execution of JavaScript. JavaScript is executed on the main thread to simplify JavaScript implementations so the JavaScript programmer doesn't have to deal with any multi-threading programming patterns.
When doing long running JavaScript computations it is running single threaded. In contrast all CPUs nowadays have multiple cores which have to be powered on while being underutilized.

## Solution [​](https://patterns.greensoftware.foundation/development/web-performance/minimize-main-thread-work/\#solution "Direct link to Solution")

For long running JavaScript computations (e.g. computations that run longer than a few 100 ms) try to use WebWorkers and run them in another thread while keeping the main rendering thread free. Consider moving the JavaScript computation to efficient server implementations that use optimized algorithms.

## SCI Impact [​](https://patterns.greensoftware.foundation/development/web-performance/minimize-main-thread-work/\#sci-impact "Direct link to SCI Impact")

`SCI = (E * I) + M per R`

[Software Carbon Intensity Spec](https://grnsft.org/sci)

Concerning the SCI equation, minimize main thread work will impact as follows:

- `E`: CPU resources can be used more efficiently which reduces the electricity required and reduces the carbon intensity

## Assumptions [​](https://patterns.greensoftware.foundation/development/web-performance/minimize-main-thread-work/\#assumptions "Direct link to Assumptions")

- An assumption is made that the code in question can be moved of the main rendering thread

## Considerations [​](https://patterns.greensoftware.foundation/development/web-performance/minimize-main-thread-work/\#considerations "Direct link to Considerations")

- Consider moving the workload to a efficient server implementation

## References [​](https://patterns.greensoftware.foundation/development/web-performance/minimize-main-thread-work/\#references "Direct link to References")

- [Main thread work breakdown](https://web.dev/mainthread-work-breakdown/)
- [What is a good Total Blocking Time](https://www.debugbear.com/docs/metrics/total-blocking-time#whats-a-good-total-blocking-time)

- [Description](https://patterns.greensoftware.foundation/development/web-performance/minimize-main-thread-work/#description)
- [Solution](https://patterns.greensoftware.foundation/development/web-performance/minimize-main-thread-work/#solution)
- [SCI Impact](https://patterns.greensoftware.foundation/development/web-performance/minimize-main-thread-work/#sci-impact)
- [Assumptions](https://patterns.greensoftware.foundation/development/web-performance/minimize-main-thread-work/#assumptions)
- [Considerations](https://patterns.greensoftware.foundation/development/web-performance/minimize-main-thread-work/#considerations)
- [References](https://patterns.greensoftware.foundation/development/web-performance/minimize-main-thread-work/#references)