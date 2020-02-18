---
title: Week 5 Planning: Machine Learning
---

# Unsupervised Methods

## Introduction

- Need a definition for ML. My understanding is that it's a collection of numeric/algorithmic methods.
- First lesson looks at unsupervised methods (only X, no Y)
- We focus specifically on two use cases:
    - Clustering
    - Dimensionality reduction

## Clustering

- _Motivation_: what are some things that we may wish to cluster in political science?
    - Sometimes, we may have an intuition that certain groups exist, and are seeking to discover them. Other times, we have no a priori expectation of groupings, and are exploring how the data can cluster.
- _Method_: Given a $j$-dimensional space, and matrix $X_{ij}$ of $i$ length-$j$ vectors, assign each vector $x_i$ to a cluster $k \in K$.
- Usually sense that members of the same cluster will be similar, and members of different clusters will be dissimilar.
    - Question: What metrics of (dis)similarity exist?
- Two examples: `k-means`, agglomerative pair-wise.
    - (_Implementation_): Review each algorithm, highlighting what makes one more efficient/scalable than the other.
- Clustering diagnostic metrics.
- Useful summary: https://www.cc.gatech.edu/~isbell/reading/papers/berkhin02survey.pdf


## Dimensionality Reduction

- _Motivation_: when would you reduce dimensionality in political science?
    - You have too many variables in your model, and are seeking to drop some.
    - You are aiming to visualise/understand some high-dimensional space.
    - You are seeking to recover some latent dimensions within your data that are not captured by your existing variables.
- _Method_: Given a matrix $X_{ij}$ of $i$ length-$j$ vectors, reduce $X_{ij}$ to $X_{ik}$ where $K \le J$.
    - In some variants, $\forall k \subset J$, in others, $\exists k \not\subset J$.
- Again, parametric vs non-parametric methods.
