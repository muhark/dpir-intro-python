---
title: "Does Microtargeting Work?"
subtitle: "Evidence from a Survey Experiment during the 2020 US Election"
author: "Musashi Jacobs-Harukawa"
institute: "Department of Politics and International Relations, University of Oxford"
date: "CESS Colloquium, 3 Nov 2021"
section-titles: false
aspectratio: 1610
mainfont: "IBM Plex Sans-Light"
---

# tl;dr

- **Objective**: estimate effect of political microtargeting.
- **Design**: Two-stage survey experiment with allocation mechanism as treatment.
- **Result**: Among unaligned respondents who had not pre-voted, targeting:
    - **Increased proportion anti-Biden by 8.7 percentage points**.
    - **Decreased proportion intending to vote Biden by 7.1 percentage points**.

## Scope 

- **Tailoring**: constructing a message so that it appeals to a specific audience.
- **Targeting**: delivering the message so only the intended audience sees it.
	- **Micro-**: on the basis of individual characteristics.

## Context

1. Rise of data-driven political campaigning in the past decade (Fowler et al 2021)
	- Creates various legal (Wood and Ravel 2017) and ethical (e.g. Burkell \& Regan 2019) issues.
2. Many of these arguments presume that micro-targeting _works_:
    - "micro-targeting of voters can pay very handsome electoral dividends for a relatively modest investment" (Krotoszynski Jr. 2020).

## Puzzle

3. Research on _psychometric profiling_ indicates that improvements should be possible (Zarouali et al 2020)
4. But extant political science research casts doubt (Nickerson and Rogers 2020)
	- Decade of political science research finds largely small/null effects of campaigns (Kalla and Broockman 2018)
	- Coppock et al (2020) find **lack of heterogeneity that leaves little room for targeting to operate**.

## Question

- _If ad effects are small and homogeneous, then how can targeting yield any benefits?_
- _Does (micro)targeting work?_

::: {.notes}
Note that in this context, I take "micro" to mean on the basis of individual traits, as opposed to group-level data.
:::


# Research Design

## Design Summarized

::: {.columns}
:::: {.column width="30%"}
**Stage 1**

- Control
- N = 1500
- 5 ads
- Random allocation
::::
:::: {.column width="40%"}
**Switch-Over**

- 5 algorithms trained on stage 1 data learn:
- Biden fav. <br>= f(ad, traits)
- Best algorithm uploaded
::::
:::: {.column width="30%"}
**Stage 2**

- Treatment
- N = 900
- Allocate ad that minimizes Biden favorability
::::
:::

## Advertisements

| Title                           | Description                                 |
| ------------------------------- | ------------------------------------------- |
| "They Mock Us"                  | In-group: Clinton and Biden mocking         |
| "Why did Biden let him do it?"  | Hunter Biden's ostensible corruption        |
| "Biden will come for your guns" | 2A; Biden will steal guns                   |
| "Insult"                        | Biden: Black Trump supporters not Black     |
| "Real Leadership"               | Obama/Biden caused wars, neglected veterans |

## Covariates

::: {.columns}
:::: {.column}
**Demographic (5 items)**

- Age
- Gender
- Race
- Income Group
- State
::::
:::: {.column}
**Political (4 items)**

- News interest
- Is country on right track?
- Partisanship (1-7 Dem/Rep)
- Ideology (1-5 L/R)
::::
:::

:::{.fragment}
_Note_: expectation that online advertisers (e.g. Facebook) able to infer these traits with high degree of accuracy.
:::

## Five Candidate Algorithms

Chosen for speed and ability to learn highly conditional relationships:

- \*Random Forest (RF)
- AdaBoost
- Gradient Boosted Decision Trees (GBDT)
- Multi-Layer Perceptron Regressor (MLPR)
- Support Vector Machine (SVM)

## Outcomes

1. Trump and Biden Favorability (1-5)
2. Voting Intention:
	- Trump/Biden/Other
	- Already voted (Trump/Biden/Other)
	- Do not intend to vote

## Hypotheses

- Targeting anti-Biden ads decreases:
	- Biden favorability
	- Intent to vote Biden
	- Intent to vote (turnout
- Versus group that receives ad at random

- All hypotheses tested conditional on partisanship (motivated reasoning)

# Results

## {data-background="figures/effect_of_targeting_presentation.png" data-background-size="contain"}

## Robustness

- Pre-treatment covariate balance check.
- Multiple comparisons correction (Holm, Benjamini-Hochberg).
- Variety of operationalizations of outcome (linear, binary, ordered categorical)
- Pre-experimental power check using Coppock et al (2020) data (along with permutation test for bias in mechanism).

## Decomposition

- Proportion of ads varies between stages.
- Effect can be decomposed:
	- "Better Allocations": leveraging within-respondent heterogeneity to increase average effect
	- "Better Ads": more of better ads shown
- Targeting vs simple A/B testing.


## {data-background="figures/heterogeneity_presentation.png" data-background-size="contain"} 


# Discussion

## Limitations

- Survey response vs vote choice
- Convenience sample
- Possible confounding due to sequential assignment.
- "Black box" approach

## Envelope Calculation

- 7.1pp decrease in unaligned voters voting Biden
- Sufficient to change outcome in Arizona (35.1% unaligned, 0.3% margin)
	- Unrepresentative sample
	- Decay

## Contradictory?

- I argue consistent with results of Coppock et al. (and others).
- Difference may be due to ML search of covariate space to maximise effect.
- In future, necessary to consider within-respondent heterogeneity?

## What We Learned

- _Possible_ to increase the effectiveness of ad campaigns with (micro)targeting.
	- Creates bad incentives for data harvesting
	- Targeting negative ads = manipulative?

# What's Next

## Follow-Up: Fixes

- **Setting**: US 2022 mid-term elections
- **Fixes**:
	- Stage 1 as training-only (avoid confounding)
	- General appeal and GOTV ads as control.
	- Increase $N$, exclude partisan respondents.

## Follow-Up: Additions

- How does priming respondents to presence of targeting moderate effect of targeting?
	- Do existing "warnings" have any effect?
	- Would a stronger disclosure have an effect?
	- How can this be used for better regulation of online ads?

## Other Applications

- Dynamic optimal allocation:
	- Continuously updating adaptive treatment design?
- Idea: maximising sample efficiency for estimating HTEs in multi-intervention studies.

## Bonus: Technical Implementation

- Built/hosted website on AWS Lightsail instance running Linux/Nginx/PHP/MariaDB (LEMP) stack.
- Responses sent real-time to to server-side kernel and db.
- Python kernel API modified Jupyter interface.
- Kernel hosts pre-trained algorithm, sends best ad back.
- PHP generates webpage to contain assigned video.
- Source code available: `https://github.com/muhark/dotas-design`
