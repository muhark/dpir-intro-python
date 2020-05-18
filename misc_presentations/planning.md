---
title: DPhil Seminar Planning
author: Musashi Harukawa
date: 14 May 2020
---

# Overview

Presenting two/three papers:

- An Information Theoretic Approach to Measurement Inference
- Micro-targeted Political Campaigns:
    - Does it work?
    - Does the effect persist when subjects are informed of the targeting?
    - Which covariates provide the most information about the predicted effectiveness of an ad?

Present in above order.

# Paper 1: Mutual Information as a Concept Measure

Slides:

- Context: Peterson & Spirling (2018), Goet (2019). Classifier Accuracy as a Quantity of Substantive Interest
    - Outline core of paper: interpretation of classifier accuracy as measure of polarization in parliament.
    - What I like about this: non-linear approaches to measurement, measurement from complex high-dimensional data
- Shortcomings:
    - Measurement Theory: explain link between concepts, indicators and measures
    - Show possibility for erroneous measurement inference "OVB".
    - Show that ideally we would minimally want to be able to "partial out" the link between confounding concepts and our measures.
- Solution:
    - Brief outline of solution.
    - A few slides on information theory.
    - Explanation of how "partialling out" information works.
    - Argue that mutual information may be a better metric in their implicit measurement model than classifier accuracy.
- Empirical Application:
    - Apply this model to their data, as well as related papers (Dutch parliament, US Congress).
- Broader relevance:
    - Frequent claims (implicitly) of the form "what does knowing X tell us about the value of Y". Information Theory gives a formalisation of these relationships that is functionally agnostic.

# Paper 2 & 3: Micro-targeting

Papers 2 and 3 share the same broader context, and will rely on the same experiment.

Slides:

## Context

- Multiple strands of related literature:
    - Law: (Big Data, etc.)
    - Psychology: (2 refs)
    - Negative Campaigning (Ansolabhere, Fridkin and Kenney AJPS 2011)
- Too many papers simply assert that micro-targeting simply works.
    - Closest thing to a test uses ABM.

## Three Research Questions

- _Does micro-targeting work?_
- Many people are aware that they are being targeted, at some level; _how do we engage critical and skeptical engagement?_
- _What information is most useful to political campaigns when seeking to micro-target?_

## Experiment

- Two-stage design:
    - Stage 1: Randomly assign treatment to one of five ads. Determine MATE of each ad as function of all covariates, and get five fitted models predicting treatment effect as a function of covariates.
    - Stage 2: Treatment now defined as being targeted. Control gets random ad, treatment gets ad predicted to have strongest effect. Two more treatment groups where subject is told beforehand that ad is selected for them.
- What does this show?
    - Stage 2: T1 - C = Microtargeting Effect
    - Stage 2: T3 - T1 = Skeptical Engagement
    - Stage 2: dMI(X_i, Y)/dX_i = Marginal Mutual Information Gain of Covariate

## Normative Territory

A few conclusions that may give us pause for thought:

- _Political campaigns are able to more effectively persuade voters when they know more about them_.
- _This effect is conditional on voters not being fully aware of the extent to which this message is being tailored specifically for them_.
- _Certain information allows campaigns to be more effective at persuading_.

My views:

- The use of personal data in campaigning should be heavily regulated, especially when combined with negative campaigning.
- Individuals should always be aware of the basis upon and extent to which a message has been tailored for them.
- Certain kinds of information about individuals should not be stored or leveraged by private or public organisations. There are a multitude of ethical concerns about privacy, etc.; I think a consequentialist view that some kinds of information allow for easier manipulation should be cause for regulating their usage.

## Outstanding Issues

- Negative campaign ads only?
- When and where? Is corona an issue?


# Specific Section Planning

## Primer on Measurement Theory

Measurement theory is an area of social science methodology concerned with the construction of _measures_.

Useful distinction between _concepts_, _indicators_ and _measures_.

- Concepts are (often latent) theoretical constructs. Will not provide an ontology of concepts here (ha) but Goertz is a good resource.
- Indicators are empirical phenomena, and therefore realizable, regular and measurable.
- Measures are constructs that systematize our observations of indicators, and make specific relational claims about the comparability of realizations of the indicators.

We usually have some theoretical reasons for believing that concepts are linked to indicators (maybe even causally!)

Can be generalised to the following diagram [include measurement diagram]

[Needs to be prefaced by article intro, so I can give example with polarization measure]

There are many kinds of biases and erroneous inferences that can be made; in this case I am most worried about a kind of confounding; the indicators and therefore the measure are systematically affected by a confounding factor that affects both partisan label and speech, or the link between the two. (e.g. diversity)

## Primer on Information Theory

Information Theory is a field of statisitcs/mathematics that, among other things, formalises the _information_ contained in random processes.

Some key concepts:

- Entropy (also joint and conditional)
- Mutual Information
- KL Divergence (maybe necessary?)

Entropy:

_The entropy $H_X$ of a discrete random variable $X$ with probability distribution $p(x)$ is defined as:_

$$
H_X \equiv - \sum_{x \in \mathfrak{X}}{p(x)log_2p(x)} = \mathbb{E}log_{2}[\frac{1}{p(x)}]
$$

Some examples:

- A fair coin
