---
title: Planning Week 7 - Web Scraping
---

# Some Thoughts

This lesson should cover:

- the way that the Internet and webpages work
- specific tools to navigate webpages (regex, requests, beautifulsoup)
- a more general understanding of automation and "deployment"

For good measure, I need to also include:

- the legal grey area that is web scraping, and good etiquette
- a discussion of time-saving/practicality

In addition to the commands and libraries mentioned above, I'll need to cover:

- Writing python scripts (instead of notebooks)
- `try/except` loops and error handling
- `while` loops

# Structure

- **Roadmap**
- How does the Internet work? (short version)
    - Your computer sends a `GET` request with some routing information (url, ip address) to an intermediary server (DNS).
    - The DNS forwards the request to the desired destination.
    - The webpage host server receives the request, and sends back the requested information (via DNS, etc.). This information is usually a mixture of `html`, `css`, `javascript` and maybe `php`.
        - `html`: The skeleton and text.
        - `css`: The aesthetic styling elements.
        - `javascript`: Locally-executed interactive elements.
        - `php`: Host-side interactive elements.
    - Your computer receives the information, and a specialised program known as a "browser" renders the information as a webpage.
- What kind of information is stored in webpages that we, as social scientists, might want to use?
    - News articles (news websites) (*ALL* news articles since _x_ date.)
    - Press releases (corporate, political) (*ALL* press release by politician _x_)
    - Government resources/archives (all parliamentary transcripts, or of a specific sub committee)
    - Tweets? (This lesson discusses APIs last)
- How can we use Python to assist us with conducting this collection on a large scale?
    - This is a task of locating, filtering and extracting information from a largely _unstructured_ dataset. For this we use:
        - `requests` to get webpages
        - `beautifulsoup` to clean up, structure and work with `html`
        - `regex` to apply flexible patterns to character-string data.
    - Added challenges are rate limiting, not knowing the format of webpages, and so on.
    - Some glaring omissions:
        - `scrapy`: A library for building deployable web crawlers.
        - `selenium`: For dealing with `javascript`/creating a scraper that behaves more like a human.
- When is it (in)appropriate to scrape?
    - Web servers have limited resources for serving requests; if they try to send too much data, then they will slow down/break.
        - Most web servers have DDoS protection measures; if they see that they are receiving a large volume of requests from a particular IP, then they will block/throttle that address.
        - Even if the server does not have these measures, be considerate, and do not accidentally cyberattack somebody.
    - Scraping is not *usually* included in the ToS of a website, but may be prohibited by your ISP etc. In most cases, it is in a legal grey area.
        - Companies and governments have the option of sending a cease-and-desist, in which case scraping does become illegal.
        - Obviously you should not do anything illegal.
