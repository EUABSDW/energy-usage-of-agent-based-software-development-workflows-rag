# https://patterns.greensoftware.foundation/development/

[Skip to main content](https://patterns.greensoftware.foundation/development/#__docusaurus_skipToContent_fallback)

✨ We've redesigned the Green Software Patterns catalogue. Browse by [Software Lifecycle](https://patterns.greensoftware.foundation/architecture) or explore patterns for [your role](https://patterns.greensoftware.foundation/personas).

Coding and implementation patterns that improve efficiency and reduce the environmental impact of software.

23 patterns

[Avoid an excessive DOM size\\
\\
The greater the amount of nodes that are defined in HTML, the greater the time spent processing and rendering each element.\\
\\
- size:medium\\
- web](https://patterns.greensoftware.foundation/development/web-performance/avoid-excessive-dom-size) [Avoid chaining critical requests\\
\\
Most web experiences require a lot of work from the user's browser. The greater the length of the chains and the larger the download sizes, the more significant the impact on page load performance and the energy required to render a page.\\
\\
- size:medium\\
- web](https://patterns.greensoftware.foundation/development/web-performance/avoid-chaining-critical-requests) [Avoid tracking unnecessary data\\
\\
User tracking, user data collection and targeting in things like advertisements are responsible for significant energy use in many digital products, and services.\\
\\
- size:small\\
- storage](https://patterns.greensoftware.foundation/development/data-handling/avoid-tracking-unnecessary-data) [Cache static data\\
\\
From an energy-efficiency perspective, it's better to reduce network traffic by reading the data locally through a cache rather than accessing it remotely over the network. Shortening the distance a network packet travels means that less energy is required to transmit it. Similarly, from an embodied carbon perspective, we are more efficient with hardware when a network packet traverses through less computing equipment.\\
\\
- networking\\
- size:small](https://patterns.greensoftware.foundation/development/data-handling/cache-static-data) [Compress stored data\\
\\
Storing uncompressed data wastes bandwidth and increases storage capacity requirements; applying appropriate compression reduces both storage consumption and the energy needed to read and write it.\\
\\
- cloud\\
- size:medium](https://patterns.greensoftware.foundation/development/data-handling/compress-stored-data) [Compress transmitted data\\
\\
From an energy-efficiency perspective, it's better to minimise the size of the data transmitted so that less energy is required because the network traffic is reduced.\\
\\
- networking\\
- size:small](https://patterns.greensoftware.foundation/development/data-handling/compress-transmitted-data) [Defer offscreen images\\
\\
Web pages offer a lot of images that aren't displayed on the first loaded screen and can thus be loaded dynamically.\\
\\
- size:small\\
- web](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/defer-offscreen-images) [Deprecate GIFs for animated content\\
\\
One direct replacement of the GIF is the MP4 video format which provides much smaller file sizes and higher quality at the same time.\\
\\
- size:small\\
- web](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/deprecate-gifs) [Enable text compression\\
\\
Web browsers often communicate with web servers in a human readable format. These can be HTML, JavaScript and/or CSS files and REST requests which can return a response in JSON. This human readable communication is redundant and, as such, can be compressed to save bandwidth.\\
\\
- size:small\\
- web](https://patterns.greensoftware.foundation/development/web-performance/enable-text-compression) [Keep request counts low\\
\\
Accessing a web page usually retrieves a HTML file from the web server. The HTML may then reference additional resources that the browser has to download.\\
\\
- size:medium\\
- web](https://patterns.greensoftware.foundation/development/web-performance/keep-request-counts-low) [Leverage pre-trained models and transfer learning for AI/ML development\\
\\
As part of your AI/ML process, you should evaluate using a pre-trained model and use transfer learning to avoid training a new model from scratch.\\
\\
- ai\\
- machine-learning\\
- size:small](https://patterns.greensoftware.foundation/development/pre-trained-transfer-learning) [Minify web assets\\
\\
Minification removes unnecessary or redundant data without affecting how the resource is processed by the web browser.\\
\\
- size:small\\
- web](https://patterns.greensoftware.foundation/development/web-performance/minify-web-assets) [Minimize main thread work\\
\\
Long-running JavaScript on the browser's main thread underutilises multi-core CPUs; offloading heavy computations to Web Workers or server-side implementations reduces energy consumption and improves efficiency.\\
\\
- compute\\
- size:small\\
- web](https://patterns.greensoftware.foundation/development/web-performance/minimize-main-thread-work) [Minimize the total number of deployed environments\\
\\
In a given application, there may be a need to utilize multiple environments in the application workflow. Typically, a development environment is used for regular updates, while staging or testing enviroments are used to make sure there are no issues before code reaches a production environment where users may have access. Each added environment has an increasing energy impact, which in turn creates more emissions. As such, it is important to understand the necessity of each enviroment and it's environmental impact.\\
\\
- cloud\\
- deployment](https://patterns.greensoftware.foundation/development/minimizing-deployed-environments) [Optimize image size\\
\\
Ideally, the stored pixel dimensions are exactly the same, or smaller, as the display size in pixels so that no bandwidth or storage space is wasted.\\
\\
- size:medium\\
- web](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/properly-sized-images) [Reduce transmitted data\\
\\
From an energy-efficiency perspective, it's better to minimize the size of the data transmitted so that less energy is required because the network traffic is reduced.\\
\\
- networking\\
- size:small](https://patterns.greensoftware.foundation/development/data-handling/reduce-transmitted-data) [Remove unused CSS definitions\\
\\
CSS files are very complex and need energy intensive parsing and processing. Each added CSS definition increases the amount of time and processing power needed in this process.\\
\\
- size:small\\
- web](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/remove-unused-css) [Serve images in modern formats\\
\\
Modern image formats can help to reduce bandwidth, storage and computing requirements on the displaying device.\\
\\
- size:small\\
- web](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/serve-images-in-modern-formats) [Terminate TLS at border gateway\\
\\
Transport Layer Security (TLS) ensures that all data passed between the web server and web browsers remain private and encrypted. However, terminating and re-establishing TLS increases CPU usage and might be unnecessary in certain architectures.\\
\\
- cloud\\
- compute\\
- kubernetes\\
- role:software-engineer\\
- security\\
- size:medium](https://patterns.greensoftware.foundation/development/evaluate-whether-to-use-TLS-termination) [Use Asynchronous network calls instead of synchronous\\
\\
When making calls across process boundaries to either databases or file systems or REST APIs, relying on synchronous calls can cause the calling thread to become blocked, putting additional load on the CPU\\
\\
- cloud\\
- size:medium](https://patterns.greensoftware.foundation/development/use-async-instead-of-sync) [Use compiled languages\\
\\
Interpreted languages re-parse and compile code on every execution, consuming more energy than pre-compiled binaries, which perform compilation once and run more efficiently at runtime.\\
\\
- cloud\\
- programming-language\\
- size:small](https://patterns.greensoftware.foundation/development/media-and-code-efficiency/use-compiled-languages) [Use server-side rendering for high-traffic pages\\
\\
Use server-side rendering for high-traffic pages\\
\\
- web](https://patterns.greensoftware.foundation/development/web-performance/use-server-side-rendering) [Use sustainable regions for AI/ML training\\
\\
Depending on the model parameters and training iterations, training an AI/ML model consumes a lot of power and requires many servers which contribute to embodied emissions.\\
\\
- ai\\
- machine-learning\\
- size:small](https://patterns.greensoftware.foundation/development/leverage-sustainable-regions)