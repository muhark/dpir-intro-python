---
title: Introduction to Python for Social Science
subtitle: Lecture 8 - APIs and Selenium
author: Musashi Harukawa, DPIR
date: 8th Week Hilary 2021
---

# Lecture Roadmap

## Last Week

- HTTP requests and Internet fundamentals
- Regular Expressions

## This Week

- APIs
	- Twitter's Academic Track
- Browser Automation

# APIs

## What is an API?

- _Application Programming Interface_
- _Interface_: Specialized endpoint
	- Specific query syntax
	- Returns defined data packets
- We are interested in _Web APIs_

## Web API Examples

- Twitter
- Reddit
- NY Times
- The Guardian
- Spotify
- Netflix

## API Mechanics

- REST vs SOAP
- RESTful APIs loosely based on HTTP methods
	- Accept HTTP-like requests to access server-side assets
	- Return the payload usually as JSON or XML
	- _Stateless_: no server-side session information

::: notes
- Most of the APIs I have come across are REST; all I know about SOAP is that it mandates XML payloads.
- Loosely-based: depending on the API, may allow for header or body parameters that do not typically exist in HTTP requests.
- Payload: the actual data packet. Sounds dramatic, it's just the thing you wanted (versus the header, which basically says what it is and where it should go).
- Stateless: remember that the server does not remember who its speaking to. That means your credentials need to be sent with each request, and importantly for paginated requests, a "next page" token. We'll come back to that later.
:::

## Twitter's API

- Many different Twitter APIs and endpoints (Standard, Premium, Enterprise, and **Academic**)
- **Academic Research product track** has following endpoints:
	- _Full-archive search_: (Almost) everything back to 2006!
	- _Recent search_: Last 7 days, higher volumes
	- _Filtered stream_: Real-time filtered stream, capped at 1% of total volume
	- _Sampled stream_: $~1\%$ of all new Tweets in real-time
	- _Tweet and User Lookup_: Look up user/tweet by id
	- and [more](https://developer.twitter.com/en/solutions/academic-research/products-for-researchers)

## Applying for Access

- The Academic Research track has the following criteria:
	- Master's student or above (doctoral candidate, post-doc, faculty, researcher, etc.)
	- Clearly defined research objective and specific plans for how you will use the Twitter data
	- Non-commercial use
- You can apply [here](https://developer.twitter.com/en/portal/petition/academic/is-it-right-for-you)

## Using the API (with Python)

- We can use Python to generate requests to interact with Twitter's API
- Twitter provides a "wrapper" package: `searchtweets-v2`
- Documentation provided [here](https://pypi.org/project/searchtweets-v2/) and [here](https://developer.twitter.com/en/docs/twitter-api/tweets/search/introduction)

## Managing Credentials

- Once you are granted access, you will be given a set of credentials for your project/application.
- Store these securely, i.e. do not post them somewhere public.
- Place them in a credentials `yaml` file that looks like the following:

:::{.fragment}
```{yaml}
search_tweets_v2:
  endpoint:  https://api.twitter.com/2/tweets/search/all
  consumer_key: <CONSUMER_KEY>
  consumer_secret: <CONSUMER_SECRET>
  bearer_token: <BEARER_TOKEN>
```
:::

## Writing and Sending Requests

- To be discussed in the coding tutorial

# Browser Automation

## When does static scraping fail?

- Sometimes the information you need is not contained in the `html` returned by a request.
- Obtaining that information may require interaction with the web app.
	- Log in
	- Dynamic elements
- Some web servers block suspicious activity

## Static vs Dynamic Webpages

- Interactive $\not\to$ Dynamic
- Dynamic page source generation
	- Server-side: `php`
	- Client-side: JavaScript

::: notes
- `html` supports moderate interactivity, through drop-down menus and text boxes
- What we're talking about here is pages with dynamic source, i.e. when you interact with an element, the source of the page itself transforms.
:::

## Browser Automation

- [Selenium Browser Automation Framework](https://www.selenium.dev/)
- Designed for testing, but useful for scraping!
- Any and all browser actions can be emulated/automated.

## Using Selenium

- Actions are methods of a "WebDriver" object.
- Many similar methods to `BeautifulSoup` for navigating DOM.
	- Search for elements by id, regex, xpath, etc.
- Selenium IDE allows you to record your own usage and codify it afterwards.

## Considerations

- Race conditions—"wait"s are your friend!
- Overhead/overkill
- Human-like automation

# Course Recap

## Topics

1. Introduction to Python and the Development Environment
2. Data Structures and `pandas` I
3. Data Structures and `pandas` II
4. Data Visualisation
5. Machine Learning with `scikit-learn` I
6. Machine Learning with `scikit-learn` II
7. Web Scraping with `BeautifulSoup` and `regex`
8. Web Scraping with `Selenium`

## You can now:

- Write and execute code using Google Colab notebooks
- Read, write, clean, and analyze different tabular data formats
- Generate summary statistics and run simple linear algebra operations
- Create static, 2D data-based visuals
- Implement, fine-tune and interpret a range of ML models
- Flexibly search text with regex
- Scrape static and dynamic webpages, and use APIs
