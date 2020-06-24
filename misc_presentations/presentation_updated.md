---
title: Information, Microtargeting and Skepticism
subtitle: Research Proposal and Outline
author: Musashi Harukawa
date: 19 May 2020
---

# Introduction

## Two Themes

Two broad themes in my research:

- **Methodological**: Feature Selection and Measurement in Complex Data Structures
- **Substantive**: Microtargeted Political Campaigning

## Three Papers

1. _Information Theoretic Approaches to Model Testing and Measurement_: Social Science Applications of Mutual Information and its Estimators
2. _This Ad was Tailored for You_: Quantifying the Microtargeting Effect and Inducing Informed Skepticism
3. _tbd_

## Questions Before I Start

- _What to expect?_
    - As I have no empirical results yet, this presentation will be mostly about design and methodology.
- _What feedback is useful?_
    - Paper 1: Relevance and clarity
    - Paper 2: Experimental design, normative aspects

# Paper 1

## Information Theoretic Approaches to Model Testing and Measurement - Social Science Applications of Mutual Information and its Estimators

## Context

- This paper began as a response to what I see as the shortcomings of a method first presented in Peterson and Spirling (2018), "Classification Accuracy as a Substantive Quantity of Interest: Measuring Polarization in Westminster Systems".
- It has since evolved into a much more broadly framed paper responding to a wider body of literature.

## Objective

As it currently stands, this paper argues: _Information theoretic statistics are straightforward to implement and interpret, and researchers can benefit from incorporating them into their research designs when asking the following kinds of questions:_

- Which (set of) factors best explains my outcome?
- What does change in the informative of $X$ on $Y$ say about the underlying states that produced both $X$ and $Y$?

## _Information Theoretic Statistics_

This refers primarily to Shannon's Mutual Information (Shannon 1948) and an estimator of this statistic (MIC, Reshef et al 2011).

Compared with more widely-used statistics, the advantage of MIC is that it is _intuitive_, _powerful_ and _equitable_ (Reshef et al 2016).

- _Intuitive_: MIC measures theoretically meaningful concepts of information and uncertainty.
- _Powerful_: able to detect and identify statistically dependent relationships between random variables **regardless of the non-linearity of the relationship**.
- _Equitable_: generates scores that measure similar strengths of relationship regardless of the functional form of the relationship.

## Research Design 1 - What explains $Y$?

Sometimes research questions ask _which independent variables are relevant to their outcome_.

- "what best explains vote choice in Britain?" (Fieldhouse et al 2019, Chapter 9)
- "which factors do (not) explain breakdown of democracy in Latin America" (Mainwaring and Perez-Liñán 2013)

Answering this requires a statistical test that accepts variables that are linked to the outcome and rejects those that are not.

I argue that MIC is a better candidate for these kinds of tests than the typical candidates, such as R-squared, Deviance, Log-Likelihood or AIC, because it is less likely to reject variables due to model misspecification.

## Research Design 2 - Informativeness of $X$ on $Y$

Sometimes the relationship between the independent and dependent variables itself varies geographically or longitudinally, _and the strength of this association is the quantity of interest_. Examples include:

- Measuring polarisation (Peterson and Spirling 2018)
- Assessing changing frames in voter judgments (Jerit and Barabas 2011).

I argue that information theoretic statistics allow researchers to:

-  make valid and intuitive claims about the nature of this relationship over time
-  control for the effect of confounders to this relationship
-  minimise the risk of erroneous inference due to model misspecification.

# Primer in Information Theory

## Overview

- The first point that I will try to make is that mutual information and its estimator MIC estimate a quantity that is both intuitive and theoretically useful.
- The second point I will try to make is that this can be easily estimated and incorporated into research designs.
- This section explains their derivation and gives a number of examples illustrating what quantity this statistic actually captures.

## Information Theory

- First detailed in Shannon (1948), Mutual Information is one of a number of statistics that is at the core of a sub-field of probability known as Information Theory.
- Concerned with formalising the information and uncertainty contained in random processes.
- Applications are widespread, from electrical engineering and the design of efficient encodings on noisy channels, to machine learning and algorithm design.

## Four Pre-requisite Concepts

Some key concepts:

- _Entropy_
- _Joint Entropy_
- _Conditional Entropy_
- _Mutual Information_

<aside class="notes">I use the definitions, theorems and formulas as written in Ash (1965), and therefore follow their notational conventions. Unless otherwise noted, all definitions, theorems and examples are either directly copied or adapted from this text.</aside>

## Entropy - Definition

_Entropy_ is a measure of the uncertainty of a random variable. The entropy $H_X$ of a discrete random variable $X$ with probability distribution $p(x)$ is defined as:

\begin{align*}
    H(X) &\equiv - \sum_{x \in X}{p(x)\,log_2\,p(x)} \\
         &= \mathbb{E}[log_{2}\,\frac{1}{p(x)}]
\end{align*}

<aside class="notes">The base of the $log$ determines the units of entropy. Base 2 means that entropy is expressed in bits, and is therefore common in computer science and digital applications. However, as changing the base is a linear transformation of the formula, it does not in fact matter what base is used.</aside>

## Entropy - Intuition

Good starting point for understanding entropy is to note that there are different degrees of randomness.

Two senses in which an event or process can be more or less random, and how this randomness is related to our certainty about the post-event state of the world:

- The range of possible values that a random event might take. The greater the number of possible outcomes, the less certainty we have about what the post-event state of the world will look like.
- The relative weights (probabilities) placed on each of the possible outcomes. If a single outcome is extremely likely, and all other outcomes extremely unlikely, then we have a greater degree of certainty about the post-event state of the world.

## Entropy - Example 1

A fair coin takes two values with equal probability. Using the above formula:

\begin{align*}
    H(X) &= -\frac{1}{2}log_2(\frac{1}{2}) - \frac{1}{2}(log_2\frac{1}{2}) \\
         &= -log_2(\frac{1}{2}) \\
         &= -(-1) \\
         &= 1 \\
\end{align*}

A fair coin therefore encodes an entropy of _1 bit_.

## Entropy - Example 1 cont.

Compare this to a fair six-sided die:

\begin{align*}
    H(X) &= -6(\frac{1}{6}log_2(\frac{1}{6})) \\
         &= -log_2(\frac{1}{6})
\end{align*}

which encodes approximately 2.584 (3 s.f.) bits of entropy. This is greater than 1 bit, reflecting that we are less certain about the outcome of a six-sided die than a fair coin.

## Entropy - Example 2

A Bernoulli random variable $X$ is distributed:

$$
f(k;q) =
    \begin{cases}
        q     & \text{if $k = 1$}, \\
        1 - q & \text{if $k = 0$}.
    \end{cases}
$$

its entropy is:

$$
    H(X) = -qlog_2q - (1-q)\,log_2\,(1-q)
$$

## Entropy - Example 2 visualised

![Bernoulli Entropy](fig_bernoulli.png)

<aside class="notes">It can be seen here that when $q=0$ or $q=1$, the outcome is certain, and therefore entropy $H(X)=0$. On the other hand, $H(X)$ is maximised at $q=0.5$, because then we are the least certain about what value $X$ might take. From these two values it should be clear that entropy captures the degree to which the outcome of a random variable is uncertain.</aside>

## Entropy as Information

- Higher entropy indicates less _a priori_ information on the realised value of a random variable.
- In the above examples, knowledge of the range of outcomes and probability density functions of the random variables determined the value of entropy.
- If, as in many cases in empirical research, pdfs and ranges are estimates with associated uncertainty, then entropy captures the information we have on the likely value of the random variable once it realises.

## Entropy as Binary Questions

A useful interpretation of entropy as a measure of information provided in Ash (1965) is as the lower bound of the average number of questions required to determine the realised value of a random variable.

Using the above examples, a fair coin requires exactly one question ("_Is it heads?"_) to determine the outcome. A fair six-sided die requires on average 2.584 (3 s.f.) questions:

## Entropy as Binary Questions cont.

```
- X>3?
    - Yes:
        - X>2?
            - Yes: ------> X=3 (P=1/6, 2 Qs)
            - No:
                - X>1?
                    - Yes: X=2 (P=1/6, 3 Qs)
                    - No:  X=1 (P=1/6, 3 Qs)
    - No:
        - X>4?
            - Yes:
                - X>5?
                    - Yes: X=6 (P=1/6, 3 Qs)
                    - No:  X=5 (P=1/6, 3 Qs)
            - No: -------> X=4 (P=1/6, 2 Qs)
```

$$
(\frac{1}{6}+\frac{1}{6})2 + (\frac{1}{6}+\frac{1}{6}+\frac{1}{6}+\frac{1}{6})3 = 2.66 > 2.584
$$

<p class="notes">The proof of this theorem is beyond the scope of this paper, but the intuition is that _uncertainty_ is measured by the number of questions required to eliminate the uncertainty, and entropy is the minimum average number of questions required to remove that uncertainty.</p>

## Joint Entropy

The _joint entropy_ of two random variables $X$ and $Y$ is given by:

$$
    H(X, Y) \equiv -
      \sum_{x \in X, Y \in Y}
      p(x, y)\,log_2\,p(x, y)
$$

## Joint Entropy in n Variables

This definition can be expanded to $n$ random variables $X_1, X_2, ..., X_n$:

$$
    H(X_1, X_2, ..., X_n) = -
    \sum_{x_1, x_2, ..., x_n}
        p(x_1, x_2, ..., x_n)\,log\,p(x_1, x_2, ..., x_n)
$$

Where $p(x_1, x_2, ..., x_n) = P\{X_1=x_1, X_2=x_2, ..., X_n=x_n\}$ is the joint probability distribution of $X_1, X_2, ..., X_n$.

<aside class="notes">Put simply, joint entropy is the simple extension entropy applied to joint events and joint probability distributions. The intuitions here are essentially the same.</aside>

## Joint Entropy and Entropy

Note that $H(X, Y) \le H(X) + H(Y)$, with equality if and only if $X$ and $Y$ are independent.

A straightforward example is the joint entropy of $M$ independent fair coin flips. This has $2^M$ outcomes and an entropy of $M$ bits. To the extent that the events are not independent, the entropy _decreases_, as there is less overall randomness.

## Conditional Entropy

The _conditional entropy_ of $Y$ given $X$ is defined as a weighted average of the entropies $H(Y|X=x_{i\in M})$:

\begin{align*}
    H(Y|X) &\equiv p(x_1)H(Y|X=x_1)+ ... + p(x_M)H(Y|X=x_M) \\
           &= - \sum^M_{i=1}p(x_i)\sum^{L}_{j=1}p(y_j|x_i)log\,p(y_j|x_i) \\
           &= - \sum^M_{i=1}\sum^{L}_{j=1}p(x_i, y_j)\,log\,p(y_j|x_i)
\end{align*}

where $L$ and $M$ are the supports over $Y$ and $X$ respectively.

## Conditional Entropy in n Variables

Conditional uncertainties concerning more than two random variables are similarly defined:

\begin{align*}
    H(Y,Z|X) &= -\sum_{i,j,k}p(x_i, y_j, z_k)\,log\,p(y_j, z_k|x_i) \\
             &= \text{the uncertainty about Y and Z given X} \\
    H(Z|X,Y) &= -\sum_{i,j,k}p(x_i, y_j, z_k)\,log\,p(z_k|x_i, y_j) \\
             &= \text{the uncertainty about Z given X and Y}
\end{align*}

## Theorem - Joint and Conditional Entropy

Conditional entropy is related joint entropy by the following theorem:

$$
    H(X, Y) = H(X) + H(Y|X) = H(Y) + H(X|Y)
$$

This result is generalisable to $n$ random variables:

\begin{align*}
    H(X, Y, Z) &= H(X) + H(Y|X) + H(Z|X, Y) \\
               &= H(X, Y) + H(Z| X, Y) \\
               &= H(X) + H(Y, Z | X)
\end{align*}

And so on.

<!-- $$
    H(X_1, ..., X_n, Y_1, ..., Y_m) = \\ H(X_1, ..., X_n) + H(Y_1, ...,Y_m|X_1, ..., X_n)
$$ -->

## Intuition - Joint and Conditional Entropy

- The joint entropy of two events can be decomposed into the entropy of one of the events plus the entropy of the other conditional on the realisation of the former.
- In other words, the extent of uncertainty over two events _A_ and _B_ can be thought of as either the uncertainty surrounding _A_ plus the uncertainty of _B given A_, or vice versa.
- Similarly, the uncertainty of _A given B_ can be understood as the combined uncertainty of _A and B_ minus the uncertainty of _B_.

## Theorem - Conditional Entropy and Entropy

Using this result, we can show that $H(Y|X) \le H(Y)$ with equality if and only if X and Y are independent. The proof follows easily from two of the previous results:

- $H(X, Y) = H(X) + H(Y|X)$ and
- $H(X, Y) \le H(X) + H(Y)$ with equality if and only if $X$ an $Y$ are independent

Therefore $H(Y|X) \le H(Y)$ with equality if and only if X and Y are independent.

## Intuition - Conditional Entropy and Entropy

This reveals a final key intuition:

>   _as long as two random variables are not statistically independent, knowing something about one reduces uncertainty over the other_.

The changes in uncertainty over random variables given knowledge of others is the dynamic at the heart of the measure I am building up to.

## Mutual Information

_Mutual Information_ is a measure of the amount of information shared between two variables, and is defined as:

\begin{align*}
    I(X|Y) &\equiv H(X) - H(X|Y) \\
            &= - \sum^M_{i=1}\sum^{L}_{j=1}p(x_i, y_j)\,log\,
            \frac{p(x_i)}{p(x_i|y_j)}
\end{align*}

This may be defined for the amount of information one set of random variables $X_1,...,X_n$ conveys about another $Y_1, ..., Y_m$:

$$
    I(X_1, ..., X_n|Y_1, ..., Y_m) = \\
        H(X_1, ..., X_n) - H(X_1, ..., X_n|Y_1, ..., Y_m)
$$

## Mutual Information - Symmetry

\begin{align*}
    I(X|Y) &= H(X) - H(X|Y) \\
           &= H(X) - (H(X, Y) - H(Y)) \\
           &= H(Y) - (H(Y, X) - H(X)) \\
           &= H(Y) - H(Y|X) \\
           &= I(Y|X)
\end{align*}

## Intuition - Mutual Information as Reduction in Entropy

The intuition in this measure is clearest when looking at the definition in terms of entropies:

The extent to which knowing values of $X$ is informative of the values of $Y$, is equal to the uncertainty over $X$ _minus_ the uncertainty of $X$ given $Y$ (and vice versa).

## MI - Example 3

- There is an online game _geoguesser_, in which you are placed into the Google streetview of a random place on the planet and asked to guess the longitude-latitude coordinates of the location.
- As you play, you use various visual clues to narrow the range of possible locations you might be in:
    - For instance, if you see that the street signs are written in Cyrillic, you know that you are likely in Russia, Belarus, Bulgaria, etc.
    - If the location looks very cold, then you could eliminate Bulgaria from the list.
- For each "clue" that you notice, you reduce the uncertainty (entropy) surrounding where you might be.

## MI - Example 3

- Thinking of the long-lat coordinates as a one random variable, and the language of the street signs as another, the above formula can be read:

$$
I(\text{location}|\text{language}) = H(\text{location}) - H(\text{location}|\text{language})
$$

- The information provided by knowing the language of the signs on your location is equal to the total uncertainty of where in the world you might be (anywhere with street views) minus the uncertainty of your location given that the signs are in Cyrillic.

## MI - Example 4

- Suppose that you have a loaf of bread in the oven, but your timer has broken and you do not know whether it has finished baking or not.
- In the absence of any other information, it is difficult to even make an "educated guess" about the state of the loaf in the oven.
- Various clues will provide information that helps inform these guesses, e.g. looking at your watch and having a rough idea of the time you put the loaf in will reduce the uncertainty about the state of the bread.
- The reduction in uncertainty is equal to the uncertainty over the state of the loaf minus the uncertainty over the state of the loaf _given your estimate of the time already passed_.

## MI - Example 4

- If the additional information "reveals" the state of the bread (e.g. there is smoke coming out of the oven), then $H(X|Y) = 0$, and the gain in information is equal to the total original uncertainty.
- To the extent that $X$ and $Y$ are independent, $H(X|Y) \rightarrow H(X)$, and thus $I(X, Y) \rightarrow 0$.

## MI - Intuition

Put succintly: _given two random variables, mutual information measures the extent to which the entropy of a random variable is reduced by knowing values of the other_.

By an earlier noted theorem, in the case where the two variables are independent $H(X|Y)=H(X)$, thus neither variable provides any information about the values of the other.

## Estimating Mutual Information

A major shortcoming of estimating MI for continuous random variables that researchers are required to discretize the variables by assigning its values to a number of bins, from which the population distribution of the variable is estimated.

Unfortunately, the number of bins has a non-trivial effect on the downstream analysis, and there is no clear optimal method for selecting this parameter.

## Introducing MIC

Reshef et al (2011, 2016) provide an alternative metric, _maximal information coefficient_ (MIC), which estimates MI with a grid of bin size and locations, and takes the maximum MI coefficient calculated.

The intuition behind the following is that MIC is an optimised estimate of mutual information across many possible discretizations.

## MIC - Preliminaries

Given a grid $G$ and point $(x, y)$:

- $row_G(y)$ returns the row of $G$ containing $y$
- $col_G(x)$ is analogous

For a pair $(X, Y)$ of jointly distributed random variables:

- $(X, Y)|_G$ denotes $(col_G(X), col_G(Y))$
- $I((X, Y)|_G)$ denotes the discrete mutual information between $col_G(X)$ and $row_G(Y)$

$D$ refers both to a finite sample from the distribution of $(X, Y)$

- Sometimes refers to a specific point $(x, y)$, in which case it makes sense to talk about $D|_G$ or $I(D)|_G$

For $k, l \in \mathbb{N}$:

- $G(k, l)$ denotes the set of all $k$-by-$l$ grids.

## Population Maximal Information Coefficient - Definition

The defintion demonstrates that the population MIC is a regularization of MI that penalises complicated grid and is normalised to fall between 0 and 1.

$$
MIC_*(X, Y) = sup_G \frac{I((X, Y)|G)}{log||G||}
$$

where $||G||$ denotes the minimum of the number of rows of $G$ and the number of columns of $G$.

## Maximal Information Coeficient - Definition

$MIC_*$ is the population value of the actual sample statistic we calculate, $MIC$. Given set of ordered pairs $D \subset \mathbb{R}^2$, the sample characteristic matrix $\hat{M}(D)$ of $D$ is given by:

$$
\hat{M}(D)_{k, l} = \frac{I^*(D, k, l)}{log\;min\{k,l\}}
$$

Then MIC is defined:

$$
MIC_B(D) = max_{kl \le B(n)}\hat{M}(D)_{k, l}
$$

## MIC - Visualised

![MIC Examples](https://minepy.readthedocs.io/en/latest/_images/relationships.png)

# Research Design 1

## What explains $X$?

- Though many quantitative research designs focus on estimating the effect of $X$ on $Y$, a related but overlooked question is _which $X$ explains $Y$_?
- One name for this problem in a broad sense is _feature selection_; which IVs do you include in your model explaining your DV?
- Standard quantitative social science wisdom suggests that you should choose IVs based on the theory you are testing.
- But what to do when you have multiple competing theories?

## Competing Theories

A variety of methods exist for comparing models and sets of IVs to explain your DV. In political science, these tend to be goodness-of-fit statistics:

- Fieldhouse et al. (2019) compare the R-squared of models fit with different categories of explanation.
- Mainwaring and Perez-Linan (2013) inspect the change in significance (p-value) on individual parameters across multiple specifications.

## Likelihood-Based Statistics

- Other methods, used more in econometrics, use statistics related to maximum likelihood estimates.
- Two examples are Deviance and Log-Likelihood.
- In essence, these statistics are based on _maximising the likelihood of the data given the model_.
- AIC and BIC similarly use ideas of the likelihood of the data given the model.

## Changes in Goodness-of-Fit

Suppose you fit two versions of a model, one including $X_2$ and one excluding it, and the goodness-of-fit indicators do not improve. I argue there are two possible things that could be happening:

- Uninformative Feature ($X_2$ tells us little about $Y$)
- Model Misspecification ($X_2$ matters, but not in the way you used it)

Barring _trying every possible specification of your model $f(\cdot)$, there is no way to be sure which reason is true_.

## Model Misspecification

- I do not think we can ignore the risk of model misspecification, as empirical phenomena are rarely perfectly describable with GLM.
- I do not claim to have a solution for model misspecification.

However, I argue that _in some cases our question does not require us to specify a model_.

## Information as Relevance

- Although we are accustomed to equating "what explains $Y$" with "which model best explains $Y$", a useful first step is filtering out which IVs are actually relevant.
- I argue that Mutual Information, and its estimator MIC, are satisfactory indicators of theoretical relevance:
    - If knowing $X$ does not reduce our uncertainty about $Y$, then how could it be theoretically relevant?
- Simply knowing which IVs matter is a theoretically relevant question, and an important first step in research.

## Model-Agnostic Estimation

- MI and MIC are _extremely general_ measures of statistical dependence.
- There is a trade-off from remaining agnostic to exact specification of the model $f(\cdot)$:
    - Negative: We do not recover the size, or direction of the effect of $X$ on $Y$.
    - Positive: We minimise the risk of erroneously rejecting/accepting variables due to model misspecification.

Before trying to estimate our model, we should first be checking if our IVs are informative.

## Roadmap

- Simulation: Does MIC identify/differntiate statistically dependent variables more consistently than alternative methods?
- Replication: How do the results of major works, e.g. Evans et al, Inglehart, etc., change if I first use MIC for feature selection?
    - Will I find that ideology is _not_ the only relevant predictor of vote choice in Britain in 2019?

# Research Design 2

## Informativeness as a Quantity of Substantive Interest

- This paper began as a response to what I see as the shortcomings of a method first presented in [Peterson & Spirling (2018)](https://doi.org/10.1017/pan.2017.39), "Classification Accuracy as a Substantive Quantity of Interest: Measuring Polarization in Westminster Systems".
- The paper presents a novel method for measuring polarization in parliaments.
- Their method uses the classifier accuracy of a supervised machine learning model trained on the bag-of-words representation of parliamentary speech as a measure of polarization.

## Peterson and Spirling (2018) Explained: Model

Train supervised machine learning algorithm to predict **party label of speaker** from **word frequencies in speech**.

$$
    Y_{d} = f(\mathbf{X}_{d}) + \epsilon
$$

where:

- $Y_{d}$ is the party label of the speaker of speech $d$, and $X_{d}$ is the length-$V$ vector of word counts for speech $d \in K$.
- $f(\cdot)$ is a mapping from the $V$-dimensional feature space to the binary party label space.
- $\epsilon$ is an error term.

## Peterson and Spirling (2018) Explained: Output and Intuition

- The fitted model will not always be able to infer the party label of the speaker from what they have said.
- The classifier accuracy over time is a summary of the ability of the model to infer party label based on speech.
- The intuition is that _in highly polarised parliaments, it is easier to guess the party identity of a speaker based on what they say_.
- Therefore, the accuracy of the classifier is a measure of the level of polarization.

## Peterson and Spirling (2018) Explained: Innovations and Relevance

- A common response to new measures is "ok great, now we have yet another way to measure this thing we already had fifteen measures for".
- I argue that the focus on _speech_ reveals an aspect of polarization that is not captured by looking at other indicators such as voting record.
- However, rather than a new measure of polarization, I think their use of classifier accuracy as a measure of substantive interest is more interesting and important.
- Supervised methods for latent concept measurement are extremely useful in a context where we have enormous quantities of complex trace data.

## Critiques of Peterson and Spirling (2018)

- If you think that the link between _the ease of predicting the party of a speaker_ and _polarization_ is problematic at best, I wholeheartedly agree with you.
- I think it is more helpful, however, to focus on the potential methodological contribution of their approach; substantive interpretations of meta-parameters of supervised models.
- Therefore my criticism of their work, and my proposed solution, is made with the aim of improving the method in order to achieve the goal of building valid measures from complex data in social sciences.

## Concepts, Indicators and Measures

Distinction between _concepts_, _indicators_ and _measures_.

- **Concepts** are (often latent) theoretical constructs. _Will not provide an ontology of concepts here but Goertz is a good resource_.
- **Indicators** are empirical phenomena, and therefore realizable, regular and measurable.
- **Measures** are constructs that systematize our observations of indicators, and make specific relational claims about the comparability of realizations of the indicators.

We usually have some theoretical reasons for believing that concepts are linked to indicators (maybe even causally!)

## Visualizing Peterson and Spirling (2018)

- _Concept_: Polarization
- _Indicator_: Link Between Speech and Party Label
- _Measure_: Supervised Classifier Accuracy

![Polarization Measurement Diagram](MeasurementFig1.png)

## Confounded Measurement

- A confounding concept, such as diversity, can affect the link between speeches and party label.
- Variations in classifier accuracy may be due to changes in polarization or changes in other factors.

![Confounded Measurement Diagram](ConfoundedMeasurement.png)

## "Partialling Out" Confounders

- Those familiar with multivariate regression know that for the standard approach to ruling out confounders is to include them in the model and calculate the partial derivative of the treatment holding confounders constant.
- This solution is not possible in this case because the relationship between $X$ and $p(\epsilon)$ is neither linear nor continuous.
- I want to provide a revision of this approach that:
    - is able to "control" for the "effect" of confounding concepts, and
    - does not rely on a particular functional specification of the statistical model.

## MIC vs Classifier Accuracy

- Both capture the extent to which knowing $X$ tells us the value of $Y$.
- However, MIC allows us to partial out the effect of individual features.
- No generalizable mathematical solution with classifier accuracy, although a computationally costly numerical solution is possible. However, no guarantee that this approach could provide stable estimates.

## MIC as a Quantity of Interest

- I believe their strategy provides a template for how we can use MIC as a measure of quantities of substantive interest:
    - The extent to which word choice reduces uncertainty about party identity at different point in times.
    - The extent to which race reduces uncertainty about job acceptance across different firms.

# Paper 2

## _This Ad was Tailored for You_ - Quantifying the Microtargeting Effect and Inducing Informed Skepticism

This paper leverages a two-stage experiment simulating a microtargeted campaign in order to answer the following questions:

1. Does microtargeting work?
2. Is the effect of microtargeted ads mitigated by informing voters how they are being targeted?

## Working Definition for Microtargeted Campaigning

Three Key Conditions:

- Messages are designated for mutually exclusive groups within the population.
- Messages are served by means that primarily only expose the target audience, and not others.
- Targeted groups are constructed on the basis of data points that are individual-specific, and cannot be inferred at the group level.

## Literature Gap

- The use of microtargeted campaigning by political actors has been subject of considerable media and legal attention.
- The academic attention to this matter has been multidisciplinary, from law to psychology to political theory to computer science.
- Few of these articles are sufficiently critical of the efficacy of microtargeting. As a result, many of their conclusions rest on the assumption that microtargeted campaigning _works_.
- This paper seeks to address that particular gap.

## Informed Skepticism

- The second aim of the paper is to test whether the standard text accompanying targeted advertisements, "this ad has been tailored for you", has any effect.
- It also attempts to show that a more explicit message, detailing the nature of the targeting, will activate an "informed skepticism" that allows individuals to engage with targeted messaging in a more critical manner.

## Data and Case Selection

- Data for this paper (and the following one) will be generated by a two-stage online experiment.
- My original plan was to conduct this in the United States during the run up to the 2020 Presidential Election. For reasons I will discuss at the end, this may have to change.
- The United States was chosen for the following reasons:
    - the availability of actual targeted political ads
    - the likelihood that highly sophisticated campaigns are in play
    - the salience of democratic outcomes in the US (I know, I know)

## Experiment Design

**Two-stage Survey Experiment**:

- _Stage 1_ of the survey experiment aims to collect data to fit five predictive models, one for each advertisement used in the experiment. These fitted models will be used for targeting in the second stage.
- _Stage 2_ is used to estimate the average treatment effect (ATE) of assignment to the microtargeted group, as well as assignment to the pseudo-informed and informed targeted groups.

## Stage 1 - Questions

The experiment begins with a battery of questions to gather information that can or is typically used to target voters with political ads.

Two approaches for deciding on which questions to include in the survey:

- emulate Facebook's ad targeting platform as closely as possible, or
- choose variables that the political science and psychological literatures believe are most relevant to persuasion.

The experiment aims to emulate the kind of targeting done by Facebook, so one approach is to collect as much of the their covariate set as possible.

## Stage 1 - Concerns

- _Privacy Concerns_: respondents should not be asked questions that would violate the ethical requirements of the research.
- _Truthful Response_: some respondents will naturally be hesitant or skeptical to provide this information. The more personal the questions, the more we are likely to prime respondents to the idea that they are being targeted.
- _Facebook's Secrets_: Facebook does not share its strategies or algorithms for targeting. Although we can infer some of their data sources and attempt to emulate their targeting, we do not know the functional form of their targeting model nor other sources of information being merged into their user data.


## Stage 1 - Treatment

There are five treatments in the first stage: five negative political ads. These should be:

- Released by same campaign.
- Likely to be targeted at different audiences.

Assignment to treatment is block-randomised; in order to maximise the efficiency of the sample, similar individuals will be less likely to be assigned the same treatment.

Treatment effect is pre-post difference in perception of candidate subject of negative ads, and self-reported likelihood of voting.

## Stage 1 - Outcome

Given:

- Five treatments $T_{i}$ indexed $i \in N=\{1, 2, 3, 4, 5\}$
- A pair of length-$j$ vectors $\mathbf{X}_{j}$ covariates
- The pre-post difference in candidate perception $Y$

I fit five Bayesian Additive Regression Tree (BART) models $f_{i}(T_i, \mathbf{X}_j)$:

$$
    \hat{Y}_i = \hat{f}_{i}(T_i, \mathbf{X}_j),\; \forall i \in N
$$

Where $\hat{Y}_i$ is the predicted treatment effect of exposure to treatment $i$. These predicted treatment effects are key to stage 2.

## Stage 2 - Using Predicted Effect

- The survey begins by collecting the same targeting covariates that were used to fit the models at stage 1.
- By passing their answers to these questions to the five fitted models from the previous stage, I get an predicted effect for exposure to each of the five ads.
- These predicted values are used depending on which treatment group the subject is assigned to.

## Stage 2 - Treatment Groups

1. _Control_: A random ad is provided. May be redundant, as this is identical to stage 1.
2. _Targeted Uninformed_: The ad with the highest predicted treatment effect is shown.
3. _Targeted Semi-Informed_: The ad with the highest predicted treatment effect is shown, with the caveat first shown that "this advertisement has been personalised for you".
4. _Targeted Fully Informed_: The ad with the highest predicted treatment effect is shown, with a screen explaining that the answers given in the previous section were used to decide which ad would be employed and what other kinds of individuals would or wouldn't be shown this ad, is shown prior.

## Quantities of Interest

_Difference in ATEs_: The following differences in average pre-post difference in candidate perception per-group, denoted $ATE_{group number}$ are of key interest:

- $ATE_2-ATE_1$: This quantity is the "microtargeting effect". I hypothesise that this value will be positive and significant.
- $ATE_2-ATE_3$: This quantity shows the extent to which a standard personalisation caveat moderates the effect of microtargeting.
- $ATE_4-ATE_2$: This quantity shows the extent to which explaining the targeting mediates the impact of microtargeting.

## Hypothesis 1

`Hypothesis 1` (_Microtargeting Works_): $ATE_2 > ATE_1$

If the targeted uninformed group has a higher average treatment effect than the untargeted group, then _by randomization we can claim that being microtargeted has a causal effect_. If the difference in the ATEs is insignificant, then we fail to show that microtargeting has an effect. This is still a substantively interesting conclusion.

## Hypothesis 2

`Hypothesis 2` (_Token Caveats Do Nothing_): $ATE_3 = ATE_2$

If the targeted semi-informed and targeted uninformed groups have the same average treatment effect, then _we can infer that there is no effect to including a token "this ad has been personalised for you" caveat_. If group 3 has a significantly smaller ATE than group 2, then we can infer that this caveat reduces or nullifies the microtargeting effect.

## Hypothesis 3

`Hypothesis 3.1` (_Motivated Skepticism_): $ATE_4 < ATE_2$

If the targeted fully informed group has a smaller average treatment effect than the targeted uninformed group, this indicates that informing voters of the manner in which they are being targeted nullifies or reduces the microtargeting effect. If the difference between the two groups is not significant, then we may suspect that voters, on aggregate, do not care whether they are being targeted.

`Hypothesis 3.2` (_Motivated Rejection_): $ATE_4 < ATE_1$

If the targeted fully informed group has a smaller average treatment effect than the untargeted group, this indicates that informing voters of the manner in which they are being targeted makes them react negatively to the message

## Potential Pitfalls 1

- _One advertisement outperforms the rest_: \
This depends on the five ads that I choose from the ad library, and stresses the importance of choosing ads on the basis that they appear to be targeted at different audiences, and not by how persuasive they are. However, I also want to choose ads that I think are likely to be persuasive, otherwise I will have no treatment effect whatsoever.

## Potential Pitfalls 2

- _Informing voters of how they are being targeted **and** what kinds of voters would be shown the same ad obfuscates the underlying causal mechanism_: \
I do not think that I am trying to expose the exact psychological mechanism by which informing voters of how they are being targeted results in the message having less, no, or the opposite effect. However, as I develop the normative/theoretical aspect of this paper, I may change my mind on this point.

## Other Issues

- _Scope_: The scope of my causal estimates is limited to American voters, **for the five ads that I have chosen**.
- _Corona_: I have concerns about the effect that a global pandemic will have on the content of campaigns, as well as how people react to fear-based messages. This may make it hard to justify the generalisability of my results to a non-crisis setting.

# Thanks for listening!
