# https://patterns.greensoftware.foundation/development/web-performance/enable-text-compression

[Skip to main content](https://patterns.greensoftware.foundation/development/web-performance/enable-text-compression/#__docusaurus_skipToContent_fallback)

✨ We've redesigned the Green Software Patterns catalogue. Browse by [Software Lifecycle](https://patterns.greensoftware.foundation/architecture) or explore patterns for [your role](https://patterns.greensoftware.foundation/personas).

On this page

## Description [​](https://patterns.greensoftware.foundation/development/web-performance/enable-text-compression/\#description "Direct link to Description")

Web browsers often communicate with web servers in a human readable format. These can be HTML, JavaScript and/or CSS files and REST requests which can return a response in JSON. This human readable communication is redundant and, as such, can be compressed to save bandwidth.

Web browsers and servers can communicate the compression format dynamically via the "Accept-Encoding"/"Content-Encoding" HTTP Headers. This allows the communication to dynamically switch to compression formats both sides support.

## Solution [​](https://patterns.greensoftware.foundation/development/web-performance/enable-text-compression/\#solution "Direct link to Solution")

Enable all supported compression formats on the server, allowing clients to use the best available format.

## SCI Impact [​](https://patterns.greensoftware.foundation/development/web-performance/enable-text-compression/\#sci-impact "Direct link to SCI Impact")

`SCI = (E * I) + M per R`

[Software Carbon Intensity Spec](https://grnsft.org/sci)

Enabling text compression will impact SCI as follows:

- `E`: Reducing emissions by reducing the amount of electricity needed while transferring and processing text files
- `M`: Reducing the size of the files can also reduce the storage requirements of the web page on the server

## Assumptions [​](https://patterns.greensoftware.foundation/development/web-performance/enable-text-compression/\#assumptions "Direct link to Assumptions")

- The use of web servers that allow compression formats

## Considerations [​](https://patterns.greensoftware.foundation/development/web-performance/enable-text-compression/\#considerations "Direct link to Considerations")

## References [​](https://patterns.greensoftware.foundation/development/web-performance/enable-text-compression/\#references "Direct link to References")

- [HTTP compression](https://en.wikipedia.org/wiki/HTTP_compression)
- [Information about Brotli, a common web compression algorithm](https://en.wikipedia.org/wiki/Brotli)
- [Compression Format WebBrowser Implementation Status](https://caniuse.com/?search=content-encoding)

- [Description](https://patterns.greensoftware.foundation/development/web-performance/enable-text-compression/#description)
- [Solution](https://patterns.greensoftware.foundation/development/web-performance/enable-text-compression/#solution)
- [SCI Impact](https://patterns.greensoftware.foundation/development/web-performance/enable-text-compression/#sci-impact)
- [Assumptions](https://patterns.greensoftware.foundation/development/web-performance/enable-text-compression/#assumptions)
- [Considerations](https://patterns.greensoftware.foundation/development/web-performance/enable-text-compression/#considerations)
- [References](https://patterns.greensoftware.foundation/development/web-performance/enable-text-compression/#references)