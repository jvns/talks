# Machine learning: the boring parts

by Julia Evans <br>

# How to not cry when someone asks you about a model you built 2 months ago

# Proving that they're paying you to build models for a reason

# No more handcrafted artisanal data visualizations

(@DanielleSucher)

# 

ML models are like dating: when the exciting new relationship butterflies are gone and now you've moved in together and you're arguing over whether you need to buy a new shoe rack for the front hall.

# This talk is not

* Building new models is so fun
* CHANGING THE WORLD WITH COMPUTERS
* new and exciting algorithms

# This talk

* **Later stages of an ML project:**
* what matters
* what we measure
* how to not have regrets later

# Machine learning at Stripe: fraud

```
card_number: <some valid-looking number>
name: John Doe
card_country: US
billing_address_country: Venezuela
ip_address_country: Australia
```

# It matters

* credit card fraud costs merchants money

# It's too much for humans to review

# ★★★ <br>MACHINE LEARNING <br>★★★


# 
```
card_number: <some valid-looking number>
name: John Doe
card_country: US
billing_address_country: Venezuela
ip_address_country: Australia
```

Example score: 80% likely to be fraudulent.

# The first question from the sales team is...

# Does it work?

* What's the false positive rate? 
* How much of the fraud do we actually catch?

# It matters

* credit card fraud costs merchants money
* blocking the wrong payments costs merchants money

# Does it work better than it did 6 weeks ago?

Did your new awesome idea for a feature actually help?

# Other questions:

* What data did I train on? (december 2013 - april 2014?)
* How did I split the data into a training set and a test set? (randomly? by date?)
* How did I transform my features? Did I need to lowercase the billing address country?
* What set of features did I use?
* If I trained a decision tree, did I set a maximum depth?

# Version control isn't enough

* too much discipline to commit everything
* too much time to reproduce results

# Bad practices: not evaluating your model at all

# Value added models

A model being used to decide whether or not to *fire teachers*,
discussed by Cathy O'Neil

<img
src="http://mathbabe.files.wordpress.com/2012/03/gradegrade.png?w=595">

**You don't want this to be you**

# Objections to evaluating your models

* We don't need to measure this change, we **know** it'll be better.
* We don't have time to measure
* Generic measures can't cover my particular artisanal case

# Bad practices: not evaluating your model at all

# Bad practices: Handcrafted artisanal data visualizations

Have you spent way too long wrangling matplotlib to make the graph you
want? it's boring. Having standard graphing tools is *amazing*.

# Bad practices: no standardization

* Can't compare precision/recall curve from March and ROC curve from April
* Forced us to sit down and decide what metrics are actually important

# Bad practices: throwing your evaluations away

# Tenets

1. Evaluating your model should be easy
1. Standardize your metrics
1. Don't throw away your data
1. Comparing models should be easy

# 

**&lt;/motivational speech&gt;** <br>
**&lt; reality &gt;**

# Reality

**139 models** for detecting fraudulent payments

* Standard set of metrics for **all of them**
* Can look up how well a given model performed in one click.

# What it looks like


# How it works

# 1. A standard format for results

**Only binary classifiers**


```
target     score
False      0.2
True       0.8
False      0.7
False      0.1
True       0.9
```

# 1. This lets us change our mind later

# 2. Metadata

* what git revision did it come from?
* How did I split the data into a training set and a test set? (randomly? by date?)
* How did I transform my features? Did I need to lowercase the billing address country?
* What set of features did I use?
* If I trained a decision tree, did I set a maximum depth?
* Which features were important?

# 2. Metadata: notes.txt

* exactly where did the training data come from?
* how did we filter them?
* the features importances for each feature

# 3. Put everything in s3

```
$ aws s3 ls s3://stripe-data-training
card_only_model_2014-07-07-23:26/scores.tsv
card_only_model_2014-07-07-23:26/notes.txt
card_only_model_2014-07-11-00:58/scores.tsv
card_only_model_2014-07-11-00:58/notes.txt
````

# 4. Metrics

# Things I learned

# don't throw away your data

show the new stuff!

# done > perfect

# simple solution > no solution

# having evaluations stored is *awesome*

# Thanks!
