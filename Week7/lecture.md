---
title: Introduction to Python for Social Science
subtitle: Lecture 7 - Mining the Web
author: Musashi Harukawa, DPIR
date: 7th Week Hilary 2020
---

# This Week

## Mining the Web

- This week we learn about automating data collection from the Internet.
- This is a powerful tool in your research arsenal, and a frequently sought-after skill by social science researchers.
- This also lays bare a broader goal that computational methods seek to accomplish: _automation_.

## Roadmap

- How does the Internet work? (Short version)
- What kinds of data can we collect from the Internet?
- How can Python assist us in conducting this collection on a large scale?
- When is it (in)appropriate to scrape?
- Coding Tutorial

## Final Note

The aim of this lecture/tutorial is twofold:

- To learn the _logic_ behind a web scraper: understanding how data is structured on the web.
- To learn the _mechanics_ of a web scraper: the tools for searching, selecting and filtering the data within these structures.

<p class="fragment">Writing a web scraper takes a lot of time and effort. Mastery of the tools will enable you to build these more efficiently, and focus on the _logic_ instead of the _mechanics_.</p>

# How does the Internet work? (Abridged)

## Our Experience

We are all familiar with how to access information on the Internet. We:

- Open our preferred browser.
- EITHER:
    - Type in the `URL` of the website we want to visit, OR
    - Type a query into our preferred search engine.
- Navigate the webpage with scrolling and clicks until we find what we want.

<p class="fragment">To understand how to automate this process, we need to understand which portions of this process can be _automated_.</p>
<p class="fragment">To understand this, let's look under the hood to see what actually happens.</p>

## STEP 1: **REQUEST**

When you type a website into your browser's `URL` bar and hit `enter`:

- Your computer sends a hypertext transfer protocol (secure) (`HTTPS`) `GET` request to the specified `URL`.

<p class="fragment">Let's break this down:</p>

- Protocol: `HTTP(S)`
- Action: `GET`
- Destination: `URL`

## Protocol

- `HTTP` is an application-level data transfer protocol used on the Internet.
- `HTTPS` is a secured version of this protocol.
- Other protocols include `FTP` (file transfer protocol), `SSH` (secure shell), etc.

## Action

- A `GET` request is an `HTTP` request for retrieving information from the target webserver.
    - Keep this in mind: accessing a webpage is similar to requesting a book or document from a library.

## Destination: `URL`

A `URL` (uniform resource locator) is a reference to a web resource. They have the generic syntax[^3023]:

```
URI = scheme:[//authority]path[?query][#fragment]
authority = [userinfo@]host[:port]

userinfo       host      port
┌──┴───┐ ┌──────┴──────┐ ┌┴┐
https://john.doe@www.example.com:123/forum/questions/?tag=networking&order=newest#top
└─┬─┘   └───────────┬──────────────┘└───────┬───────┘ └───────────┬─────────────┘ └┬┘
scheme          authority                  path                 query             fragment
```

[^3023]: This example is taken directly from https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Generic_syntax

## `URL`s Explained

```
              host
        ┌──────┴───────┐
https://muhark.github.io/dpir-intro-python/Week7/lecture.html#/urls-explained
└─┬─┘   └──────┬───────┘└─────────────────┬─────────────────┘└──────┬───────┘
scheme     authority                     path                     fragment
```


- **scheme**: Protocol, as mentioned in the slide above.
- **authority**: Constructed of three _subcomponents_.
    - Two of them are optional (`userinfo@` and `:port`), and not seen here.
    - `host` is essentially the name of the webserver.
- **path**: A path in the internal filesystem of the webserver.
- **fragment**: Optional, "scrolls" to a specific sub-element within the webpage.

## Aside: IP Addresses, DNS

_(Heavy oversimplification on this slide)_

- The destination webserver's "location" within the Internet is stored not as a `URL`, but usually as an IP address, e.g. `216.58.210.206`
- You can think of an IP address as acting exactly like a physical address for mail.
- To make sure that your request gets sent to the right desintation the host in the `URL` must be converted to an IP address. This conversion is done by `DNS`.
    - DNS resolvers are essentially the address books of the web. They maintain records of urls and IP addresses.
    - These resolvers are within the browser, our OS, and also maintained by third parties such as our ISPs, Google or Cloudflare.
- This usually does not matter too heavily for web scraping.

## STEP 2: **RESPONSE**

Your request now having been routed to the correct address, the webserver:

- Reads the header, and accepts or declines the request.
- Reads the contents of the request (i.e. the path, query, fragment)
- Returns the data to the IP address given in the request packet header.
- Usually, this information will be in the formatted as a mixture of an `html`, `css` and `javascript`.
    - Exceptions: requesting `pdf` documents directly from webpages, interacting with a `php` server.


## STEP 3: **RENDER**

A web browser is actually a specialised piece of software that can render and display all kinds of document formats, and allow you to interact with them via a graphical interface[^788f].

Many websites you deal with will be a mixture of `html`, `css` and `javascript`.

- `html` is more appropriately described as a data structure than a language. It provides the "skeleton" of the webpage and the textual elements.
- `css` is also a data structure, but provides _styling_ information that informs much of the aesthetics of the webpage.
- `javascript` is a programming language that runs programs on the _client side_ (i.e. in your computer) and creates interactive elements on webpages.

[^788f]: There are CLI web browsers, such as `lynx`. These are fun to play around with if you want to explore the Internet without any graphical elements.

## `html`

_Hypertext Markup Language_, or `html`, is the core of all webpages.

- Consists of _elements_, beginning and ending with a _tag_.
- Nested structure (like a dictionary).

## `html` tags

- Tags define the type of element contained between them:
    - `<head>...</head>`: Defines the header block
    - `<h1>...</h1>`: Section header level 1
    - `<p>...</p>`: Paragraph
    - `<div>...</div>`: Defines a section in a document
    - For a full reference see [here](https://www.w3schools.com/TAGs/)
- The front tag can contain additional attributes:
    - `<section id="title-slide">...</section>`
    - The `class` attribute allows for style inheritance from `css`.

## `html` example

```{html}
<section id="title-slide">
  <h1 class="title">Introduction to Python for Social Science</h1>
  <p class="subtitle">Lecture 7 - Mining the Web</p>
  <p class="author">Musashi Harukawa, DPIR</p>
  <p class="date">7th Week Hilary 2020</p>
</section>
```


## Inspecting Source

Most browsers allow you to inspect the source of the webpage that you are viewing. I recommend that you use Chrome/Chromium/Firefox.

| Mac                | Windows/Linux              |
| ------------------ | -------------------------- |
| `Command+Option+I` | `F12` or `Control+Shift+I` |

The devtools in the browser allow you to inspect the `html` and `css` files that generate the webpages. Recognising how these are structured is key to web scraping.

# Web Mining for Social Scientists?

## Note on Terminology

I use the following three terms to refer to different things:

- _Web Scraping_: The automated collection of data from web pages.
- _Data Collection via API_: The automated collection of data from the web, via a server-provided API.
- _Web Crawling_: The automated traversing of web pages to search for information.

<p class="fragment">The difference will become clearer as I discuss them.</p>

## Social Science Use Cases

- Collecting parliamentary transcripts.
- Collecting pdfs of referendum texts (in Switzerland).
- Collecting government statistics (on education, for example).
- Collecting press releases.
- Gathering news articles stored online.
- Recording user interactions on Reddit.
- Gathering tweets.
- Analysing precinct-level crime data.
- ...

## Trace Data vs Embedded Structured Data

It's useful to distinguish between _trace_ data, and structured data embedded in websites.

- Trace data is incidental; it is generated by usage of online resources. Examples include Facebook or Reddit posts, website visit counts, Tweets, and so on.
    - Much of "big data" refers to massive volumes of trace data generated on a secondly basis by users on these websites.
    - Using trace data requires you to think more carefully about what exists, how that connects to the activity you are trying to measure. Missingness is less clear; it could be erased/censored entries, or offline activity.
- Embedded structured data (my term) refers to online archives of structured data. This could take the form of statistics stored in spreadsheets, transcripts of debates, and so on.
    - The objective here is entirely different; it may make sense to collect large portions of the archive and leverage other libraries to parse it afterwards.
- This is not a dichotomy; many things fall somewhere in between, such as press releases.

## APIs

Some websites provide an _application programming interface_ (API), which is an interface specifically designed for automated querying/retrieval.

- If an API exists, _use it_. APIs are more resource efficient than webpages, and exist in part to prevent unstructured scraping.
- Check for an API at the bottom of the webpage, sometimes in a section "for developers".
- There will usually be documentation for an API, and sometimes even a specific Python library (e.g. `tweepy` for Twitter).
- Because APIs are so specific to websites, I will not go over them in this class.

# Using Python for Web Mining

## Libraries

The following libraries are key for building web scrapers:

- `requests`: For making generic http(s) requests.
- `beautifulsoup`: "Cleans up" and provides powerful interface for navigating html.
- `re`: Regular expressions library for powerful string matching.

<p class="fragment">Some glaring omissions from this list:</p>

- `scrapy`: For building deployable web crawlers
- `selenium`: Web testing library, can handle `javascript` and be programmed to behave much more like a human than a bot.

## Retrieving Web Pages

Here's a function I wrote/adapted from [_Web Scraping with Python, 2nd Ed._](https://www.oreilly.com/library/view/web-scraping-with/9781491985564/)

```{python}
def safe_get(url, parser='html.parser'):
    try:
        session = requests.Session()
        headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                   "User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0"
                   }
        req = session.get(url, headers=headers)
    except requests.exceptions.RequestsWarning:
        return None
    return BeautifulSoup(req.text, parser)
```

## `try`/`except`

```{python}
    try:
        session = requests.Session()
        [...]
        req = session.get(url, headers=headers)
    except requests.exceptions.RequestsWarning:
        return None
```

`try`/`except` is a control flow structure that runs the code in the `try` block until an _exception_ occurs, and if the _exception_ is of the kind defined after `except`, then it executes the `except` block.

- In this case the function first runs the code from `session = ...` to `... headers=headers)`
- If in the execution of this code, a `requests.exceptions.RequestsWarning` is _raised_, then the code `return None` is executed.
- If a different kind of exception occurs, then it is not _handled_ by this except statement, and is raised normally (resulting in an error).

## `requests`

There are just three things the `requests` library is being used for:

- Initiating a session.
- Sending a `GET` command to the provided url with a customized header.
    - This header is copied from a standard browser, to make the request appear as a regular user (and not a bot).
- Web-request specific errors/exceptions.

## `BeautifulSoup`

## `re`

A regular expression (RegEx) is a sequence of characters that defines a _search pattern_. These patterns are used to systematically and flexibly search through strings.

Python provides its own implementation of regular expressions, along with the built-in library `re`.

## Understanding Regular Expressions

Regular expressions are constructed of:

- _regular characters_, which are the literal characters themselves
- _metacharacters_, which have special meanings

<p class="fragment">For instance, the regular expression `a.` contains:</p>

- `a`: the regular character lowercase 'a'
- `.`: the metacharacter matching any character except a newline.

## Metacharacters for Character Sets

- `.`: Any character other than `newline` (the character denoting that the subsequent character should be on a new line)
- `[]`: Defines a character set.

## Metacharacters Defining Repetition

- `*`: Matches 0 or more consecutive instances of the previous regular expression. Matches as many as possible.
- `+`: Matches 1 or more consecutive instances of the previous regular expression. Matches as many as possible.
- `?`: Matches 0 or 1 instances of the previous regular expression.
- `{m}`: Matches exactly `m` instances of the previous regular expression.
- `{m, n}`: Matches between `m` and `n` instances of the previous regular expression.

## Other Special Characters

- `^`: Matches the null character at the beginning of a string.
- `$`: Matches the null character at the end of a string.
- `\`: Converts the subsequent metacharacter to a literal.


This following pattern will match strings beginning with "comput": `comput.*`

- The letters `comput` match EXACTLY those letters.
- The `.` symbol denotes ANY non-whitespace character.
