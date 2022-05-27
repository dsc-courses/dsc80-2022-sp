---
layout: page
title: Project 5
description: Description of Project 5.
nav_exclude: true
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>


# Project 5 – Model Building 🛠
{:.no_toc}

### Due Date: Thursday, June 9th at 11:59PM (NO SLIP DAYS!)
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

Welcome to Project 5, the final assignment of the quarter! 👋

**Project 5 is due on Thursday, June 8th at 11:59PM. This is a hard deadline; you may NOT use slip days on this project.** (This is because we need to start grading projects right when you turn them in, so that there is enough time for you to make regrade requests before we submit grades to campus.) Note that we will not be able to hold many office hours during Finals Week, so make sure to start early.

Like Project 3, there is no checkpoint. **Since this project is only graded on the output displayed in a notebook (no `.py` file will be submitted)**, you will need to make sure you submit a "readable report" that graders can follow.

---

## Instructions

In Project 5, you will conduct an open-ended investigation into the dataset you chose for [Project 3](https://dsc80.com/project3) (NYPD, Stocks, or Outages). **Specifically, you will pose a prediction problem and train a model to solve it.** Use the [Example Prediction Problems](#example-prediction-problems) section for inspiration.

You will follow the steps given below. **You should summarize each of these steps using Markdown cells in the "Summary of Findings" section of your notebook.** [A template version of the notebook you must submit can be found in our GitHub repo](https://github.com/dsc-courses/dsc80-2022-sp/blob/main/projects/05-prediction/template.ipynb).

### Step 1 – Framing the Problem (15%)

Clearly state and frame a prediction problem. Explicitly mention:
- The type of prediction problem (classification or regression). If you are building a classifier, make sure to state whether you are performing binary classification or multiclass classification.
- The response variable (i.e. the variable you are predicting) and why you chose it.
- The metric you are using to evaluate your model and why you chose it over other suitable metrics (e.g. accuracy vs. F1-score).

Make sure to justify what information you would know at the "time of prediction" and to only train your model using those features. (For instance, if we wanted to predict your final exam grade, we couldn't use your Project 5 grade, because Project 5 is only due after the final exam!)

### Step 2 – Baseline Model (35%)

Train a "baseline model" for your prediction task that uses at least two features. You can leave numerical features as-is, but you'll need to take care of categorical columns using an appropriate encoding. Implement all steps (feature transforms and model training) in a `sklearn` `Pipeline`.

In your Summary of Findings, make sure to be clear about:
- The features in your model, including how many are quantitative, ordinal, and nominal, and how you performed any necessary encodings.
- The performance of your model, and whether or not you believe your current model is "good" and why. **Both now and in Step 3, make sure to evaluate your model's ability to generalize to unseen data!**

Note, there is no "required" performance metric that your baseline model needs to achieve.

### Step 3 – Final Model (35%)

Create a "final" model that improves upon the "baseline" model you created in Step 2. Do so by engineering at least two new features from the data, on top of any categorical encodings you performed in Step 2. (For instance, you may use `StandardScaler` or `QuantileTransformer` transformers on quantitative columns.) Again, implement all steps in a `sklearn` `Pipeline`.  

While deciding what model and features to use, you **must** perform a search for the best model and hyperparameters (e.g. tree depth) to use amongst a list(s) of options, either by using `GridSearchCV` or through some manual iterative method.

In your Summary of Findings, make sure to be clear about:
- The features you added and **why** they are good for the data and prediction task.
- The model you chose, the hyperparameters that ended up performing the best, and the method you used to select a model.

Note, you will not be graded on "how much" your model improved from Step 2 to Step 3. What you will be graded on is on whether or not your model improved, as well as your thoughtfulness and effort in creating features, along with the other points above.

### Step 4 – Fairness Analysis (15%)

Perform a "fairness analysis" of your final model from Step 3. That is, try and answer the question "does my model perform worse for individuals in Group X than it does for individuals in Group Y?", for an interesting choice of X and Y.

As always, when comparing some quantitative attribute (in this case, something like precision or RMSE) across two groups, we use a **permutation test**. Let's illustrate how this works with an example. Let's suppose we have a sample voter dataset with columns `'Name'`, `'Age'`, and `'Voted'`, among others. We build a classifier that predicts whether someone voted (`1`) or didn't (`0`).

Here, we'll say our two groups are
- "young people", people younger than 40
- "old people", people older than 40

Note that in this example, we manually created these groups by **binarizing** the `'Age'` column in our dataset, and that's fine. (Remember, the `Binarizer` transformer with a threshold of 40 can do this for us.)

For our evaluation metric, we'll choose precision. (In Lectures 26 and 27 we looked at other evaluation metrics and related parity measures for classifiers; choose the one that is most appropriate to your prediction task. If you built a regression model, you cannot use classification metrics like precision or recall; instead, you must use RMSE or $$R^2$$.)

Now, we must perform a permutation test. Before doing so, we must clearly state a null and an alternative hypothesis. 

- Null Hypothesis: Our model is fair. Its precision for young people and old people are roughly the same, and any differences are due to random chance.

- Alternative Hypothesis: Our model is unfair. Its precision for young people is lower than its precision for old people.

From here, you should be able to implement the necessary permutation test. The only other guidance we will provide you with is that you should **not** be modifying your model to produce different results when computing test statistics; use only your final fitted model from Step 3.

Make sure to clearly state your hypotheses, a p-value, and your conclusion of the test based on the p-value.

---

## Example Prediction Problems

Below, we provide example prediction problems for all three datasets. However, don't restrict yourself to just these – feel free to come up with your own!

### NYPD Civilian Complaints 🚔

* Predict the outcome of an allegation. (You may need to "engineer" your output column).
* Predict the complainant or officer ethnicity.
* Predict the amount of time between the month received vs. month closed (i.e. the difference of the two columns).
* Predict the rank of the officer.

### Power Outages 🔋

* Predict the severity (in terms of number of customers, duration, or demand loss) of a major power outage.
* Predict the cause of a major power outage.
* Predict the number and/or severity of major power outages in the year 2022.
* Predict the electricity consumption of an area.

### Stock Trades by Members of the US House of Representatives 📈

* Predict the party affiliation of a representative from their stock trades.
* Predict the geographic region (e.g. West Coast, South) that a representative comes from using their stock trades.
* Predict whether a trade is a BUY or SELL.

---

## Grading and Submission

Unlike in Project 3, we will **not** be providing you with the exact rubric that we will evaluate your report on. This is because an exact rubric would specify exactly what you need to do to build a model, but figuring out what to do is a large part of the project. (However, you can see how much each step is worth in the headings above.)

With that said, **you will be graded on addressing all of the above requirements in your summary.** You should have your code included at bottom in a clearly done, commented fashion. Upon reading the summary, it should be easy for the grader to glance down at the code to see the supporting work.

To submit the project, generate a **PDF of your Jupyter Notebook** that contains all of the requirements above, and upload that PDF to Gradescope. You will not need to upload the raw notebook to Gradescope. Notes:
- While working, you may keep your code in a `.py` file and import it if you'd like. Just (1) be sure the output is clearly visible in the notebook, and (2) copy and paste the code from the file to the *very* bottom of the notebook before submitting.
- To export your notebook as a PDF, first, restart your kernel and run all cells. Then, go to "File > Print Preview". Then, save a print preview of the webpage as a PDF. There are other ways to save a notebook as a PDF but they may require that you have additional packages installed on your computer, so this is likely the most straightforward.
- There are three "Project 5" assignments on Gradescope, one for each dataset. Make sure to submit to the correct one, and to tag your partner!
- A final reminder – **you cannot use slip days on Project 5**!