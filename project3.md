---
layout: page
title: Project 3
description: Description of Project 3.
nav_exclude: true
---

# Project 3 🚔📈🔋
{:.no_toc}

<span style='color: red'><b>Note: All information on this page is subject to change until the project is formally released.</b></span>

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

### Due Date

- The due date is Thursday May 12th.
* This project contains no new material and is a good opportunity to sharpen your understanding of the core concepts of the first half of the course.
* While there is no checkpoint, try to self-impose the checkpoint. This will enable you to polish your work into a coherent notebook upon submission. Since this project is only graded on the output displayed in the notebook (no `.py` file will be submitted), you will need to make sure you submit a "readable report" that graders can follow!

---

## Instructions

This project will be an open investigation into a dataset. You will follow the steps given below:

1. Pull the latest version of the dsc80 repo, this should have a `template.ipynb` file that you will use as a template for the project. If you deleted the file or want another copy of the template, it can be found here: https://github.com/dsc-courses/dsc80-2022-sp/projects/03-topic/template.ipynb
2. Pick **one** of the three datasets that can be found under the instructions ("NYPD Civilian Complaints", "Power Outages", or "Stock Trades").
3. Download the dataset of your choosing and load it into your `template.ipynb` file.
4. Narrow down a few questions and lines of inquiry to pursue in the dataset of choice.
5. Assess the quality of these datasets via exploratory data analysis, placing your results in the context of how the data were generated.
6. Assess the mechanism of missingness for some relevant portion of the dataset.
7. Ask/answer a question about the dataset using a hypothesis test or permutation test, being sure to discuss uncertainty of your result and possible shortcomings of your approach.
8. Conclude with how you might improve your work and what data you might use to do so.

<!-- ## How to Organize and Submit Your Work for Grading -->

Now that you have a rough overview of what you are going to be doing in the project, the following sections will talk about the items you will need in your project in detail so read it ***carefully***: 

### Summary of Findings
Each of these steps will be summarized in the *Summary  of Findings* section at the top of the project notebook. This should include:

* Introduce the dataset as you understand it and how it relates to the question you are investigating.
* Describe data-cleaning steps and how it affects your analyses. Steps should be explained/justified in reference to the data generating process.
* Describe the setup/results of your assessment on missingness, including how to interpret those results, your statistical confidence, and how they might affect your ability to answer questions about the dataset. 
* Describe the setup/results of your Hypothesis test, including being clear about your null/alternative hypothesis, your test-statistic, the significance level you used, and what conclusions you can draw from the results.

Each of the above should contain *specifics* about your data-analyses (e.g. concrete numbers). The work/code/details for how you obtained your results should be included in your notebook, **below** the *Summary of Findings* section. You should clearly label what you are doing in your work using the 'markdown cells' in your notebook.

### Style

When doing the work that informs your summary, **you should write organized, readable code, broken into clearly delineated sections.**

* Your work for each of the project sections described below should be completed in code cells underneath the markdown-headers of that sections name. 
* The output of each code cell (e.g. tables and plots) should have an explanation of is contained in them and why. This explanation should be:
    - Written in a markdown cell above the code when you are explaining what the output of a cell is doing and how it relates to your question.
    - Written as a code comment when explaining what the code is doing.
    - Written in the title of a plot.
* You should **only include work that is relevant** to posing, explaining, and answering the question(s) you stated in the summary. You should include data quality, cleaning, and missingness assessments, though these should broadly be relevant to the question at hand.
* Do **not** include long dataframe output; if you want to include specific data from a dataframe in the writeup, display only the `head`.

### Requirements: Cleaning and EDA (Exploratory Data Analysis)

* **Clean the data** appropriately for your question (e.g. replace data that should be missing with `NaN`, create new columns out of given ones -- e.g. compute distances, scale data, get time information from time stamps).
* **Univariate Analysis:** look at the statistics of relevant columns separately (e.g. their distribution and statistics) using tables and appropriate plots.
* **Bivariate Analysis:** look at the statistics of pairs of columns to identify possible associations. Use scatterplots, plot conditional distributions, box-plots, etc. Also, you should examine and plot pivot tables. This will best inform interesting hypothesis tests!
* **Interesting Aggregates:** Choose columns to group-by and examine aggregate statistics.

### Requirements: Assessment of Missingness

* Recall that whether data is NMAR or not is an assumption of whether the missingness is explainable by observed data or not. In this section, you will investigate the likely missingness mechanisms of your data as being missing at random. Before making this assumption, address in the summary whether you believe the data is NMAR -- explain your reasoning and any additional data you might want to obtain that could explain the missingness (thereby making it MAR).
* Pick a column with non-trivial missingness to analyze.
* Perform permutation tests to analyze the dependency of this missingness on other columns.
    - Find at least one column for which missingness is dependent and one for which missingness is not dependent.
* Interpret the meaning of the permutation test results with respect to your data and question.

### Requirements: Hypothesis Test

* Formulate a hypothesis and perform a hypothesis test. You can use the "sample lines of inquiry" in each project notebook for inspiration or you can create your own.
* Be sure to explicitly state the (null and alternative) hypothesis, the test-statistic, the significance level, the resulting p-value and results. Justify why these choices are good choices for answering the question you are trying to answer.

TODO make sure this is consistent with the fact that it's on a webpage

TODO below, you will find descriptions of the three datasets you can choose from

---

## NYPD Civilian Complaints
This project contains data on 12,000 civilian complaints filed against New York City police officers. Interesting questions to consider include:
- Does the length that the complaint is open depend on ethnicity/age/gender?
- Are white-officer vs non-white complaintant cases more likely to go against the complainant? 
- Are allegations more severe for cases in which the officer and complaintant are not the same ethnicity?
- Are the complaints of women more succesful than men (for the same allegations?)

There are a lot of questions that can be asked from this data, so be creative! You are not limited to the sample questions above.

### Getting the Data
The data and its corresponding data dictionary is downloadable [here](https://www.propublica.org/datastore/dataset/civilian-complaints-against-new-york-city-police-officers).

Note: you don't need to provide any information to obtain the data. Just agree to the terms of use and click "submit."

### Cleaning and EDA
- Clean the data.
    - Certain fields have "missing" data that isn't labeled as missing. For example, there are fields with the value "Unknown." Do some exploration to find those values and convert them to null values.
    - You may also want to combine the date columns to create a `datetime` column for time-series exploration.
- Understand the data in ways relevant to your question using univariate and bivariate analysis of the data as well as aggregations.

### Assessment of Missingness
- Assess the missingness per the requirements in `project03.ipynb`

### Hypothesis Test / Permutation Test
Find a hypothesis test or permutation test to perform. You can use the questions at the top of the notebook for inspiration.

---

## Power Outages
This project uses major power outage data in the continental U.S. from January 2000 to July 2016. Here, a major power  outage is defined as a power outage that impacted at least 50,000 customers or caused an unplanned firm load loss of atleast 300MW. Interesting questions to consider include:
- Where and when do major power outages tend to occur?
- What are the characteristics of major power outages with higher severity? Variables to consider include location, time, climate, land-use characteristics, electricity consumption patterns, economic characteristics, etc. What risk factors may an energy company want to look into when predicting the location and severity of its next major power outage?
- What characteristics are associated with each category of cause?
- How have characteristics of major power outages changed over time? Is there a clear trend?

### Getting the Data
The data is downloadable [here](https://engineering.purdue.edu/LASCI/research-data/outages/outagerisks).

A data dictionary is available at this [article](https://www.sciencedirect.com/science/article/pii/S2352340918307182) under *Table 1. Variable descriptions*.

### Cleaning and EDA
- Note that the data is given as an Excel file rather than a CSV. Open the data in Excel or another spreadsheet application and determine which rows and columns of the Excel spreadsheet should be ignored when loading the data in pandas.
- Clean the data.
    - The power outage start date and time is given by `OUTAGE.START.DATE` and `OUTAGE.START.TIME`. It would be preferable if these two columns were combined into one datetime column. Combine `OUTAGE.START.DATE` and `OUTAGE.START.TIME` into a new datetime column called `OUTAGE.START`. Similarly, combine `OUTAGE.RESTORATION.DATE` and `OUTAGE.RESTORATION.TIME` into a new datetime column called `OUTAGE.RESTORATION`.
- Understand the data in ways relevant to your question using univariate and bivariate analysis of the data as well as aggregations.

*Hint 1: pandas can load multiple filetypes: `pd.read_csv`, `pd.read_excel`, `pd.read_html`, `pd.read_json`, etc.*

*Hint 2: `pd.to_datetime` and `pd.to_timedelta` will be useful here.*

*Tip: To visualize geospatial data, consider [Folium](https://python-visualization.github.io/folium/) or another geospatial plotting library.*

### Assessment of Missingness
- Assess the missingness of a column that is not missing by  design.

### Hypothesis Test
Find a hypothesis test to perform. You can use the questions at the top of the notebook for inspiration.

---

## Stock Trades by Members of the US House of Representatives

This project uses public data about the stock trades made by members of the US House of Representatives. This data is collected and maintained by Timothy Carambat as part of the [House Stock Watcher](https://housestockwatcher.com/) project. The project describes itself as follows:

> With recent and ongoing investigations of incumbent congressional members being investigated for potentially violating the STOCK act. This website compiles this publicly available information in a format that is easier to digest then the original PDF source.
>
> Members of Congress must report periodic reports of their asset transactions. This website is purely for an informative purpose and aid in transparency.
>
> This site does not manipluate or censor any of the information from the original source. All data is transcribed by our community of contributors, which you can join for free by going to our transcription tool. Our moderation team takes great care in ensuring the accuracy of the information.
>
> This site is built and maintained by Timothy Carambat and supported with our contributors.

Some interesting questions to consider for this data set include:

- Is there a difference in stock trading behavior between political parties? For example:
    - does one party trade more often?
    - does one party make larger trades?
    - do the two parties invest in different stocks or sectors? For instance, do Democrats invest in Tesla more than Republicans?
- What congresspeople have made the most trades?
- What companies are most traded by congresspeople?
- Is there evidence of insider trading? For example, Boeing stock dropped sharply in February 2020. Were there a suspiciously-high number of sales of Boeing before the drop?
- When are stocks bought and sold? Is there a day of the week that is most common? Or a month of the year?

### Getting the Data

The full data set of stock trade disclosures is available as a CSV or as JSON at https://housestockwatcher.com/api.

This data set does not, however, contain the political affiliation of the congresspeople. If you wish to investigate a question that relies on having this information, you'll need to find another dataset that contains it and perform a merge. *Hint*: Kaggle is a useful source of data sets.


### Cleaning and EDA

- Clean the data.
    - Certain fields have "missing" data that isn't labeled as missing. For example, there are fields with the value "--." Do some exploration to find those values and convert them to null values.
    - You may also want to clean up the date columns to enable time-series exploration.
- Understand the data in ways relevant to your question using univariate and bivariate analysis of the data as well as aggregations.


### Assessment of Missingness

- Assess the missingness per the requirements in `project03.ipynb`

### Hypothesis Test / Permutation Test
Find a hypothesis test or permutation test to perform. You can use the questions at the top of the notebook for inspiration.

TODO update missingness description for stocks based on conversation and tutor feedback


---

## Rubric

TODO copy rubric from fa21 and put it here along with point values

| Component | Weight |
| --- | --- |
| Introduction | 5 points |
| idk | 25 points |


---
