---
layout: page
title: Project 3
description: Description of Project 3.
nav_exclude: true
---

# Project 3 🚔🔋📈
{:.no_toc}

### Due Date: Thursday, May 12th at 11:59PM
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

Welcome to Project 3! 👋

This project contains no new material. Rather, it's a good opportunity to sharpen your understanding of the core concepts of the first half of the course.

**The project is due on Thursday, May 12th at 11:59PM**. While there is no checkpoint, try to self-impose the checkpoint. This will enable you to polish your work into a coherent notebook upon submission. **Since this project is only graded on the output displayed in a notebook (no `.py` file will be submitted)**, you will need to make sure you submit a "readable report" that graders can follow!

---

## Instructions

This project will be an open investigation into **a single dataset**. You will follow the steps given below:

1. Pull the latest version of the [`dsc80-2022-sp`](https://github.com/dsc-courses/dsc80-2022-sp/) repo. Within the `projects/03-topic` folder, there is a `template.ipynb` notebook that you will use as a template for the project. If you delete the file or want another copy of the template, you can re-download it from [here](https://github.com/dsc-courses/dsc80-2022-sp/projects/03-topic/template.ipynb).
2. Pick **one** of the three datasets described below:
    - [NYPD Civilian Complaints](#nypd-civilian-complaints-).
    - [Power Outages](#power-outages-).
    - [Stock Trades](#stock-trades-).
3. Download the dataset of your choosing and load it into your `template.ipynb` file.
4. Narrow down a few questions to pursue in the dataset of choice.
5. Assess the quality of these datasets via exploratory data analysis, placing your results in the context of how the data were generated.
6. Assess the mechanism of missingness for some relevant portion of the dataset.
7. Ask and answer a question about the dataset using a hypothesis test or permutation test, being sure to discuss uncertainty of your result and possible shortcomings of your approach.
8. Conclude with how you might improve your work and what data you might use to do so.
9. Submit a **PDF version of your notebook** to Gradescope. More details in the [Rubric and Submission](#rubric-and-submission) section.

<!-- ## How to Organize and Submit Your Work for Grading -->

Now that you have a rough overview of what you are going to be doing in the project, the following sections will talk about the specific items you will need in your project. **Read the following sections carefully!**. 

### Summary of Findings
Each of the following steps should be summarized in the **Summary of Findings** section at the top of your project notebook. Your summary must:

* Introduce the dataset as you understand it and how it relates to the question you are investigating.
* Describe the data cleaning steps you took and how they affected your analyses. The steps should be explained in reference to the data generating process.
* Describe the setup and results of your assessment on missingness, including how to interpret those results, your statistical confidence, and how they might affect your ability to answer questions about the dataset. 
* Describe the setup and results of your hypothesis test. Make sure to explicitly state your null and alternative hypotheses, test statistic, the significance level you used, and what conclusions you can draw from the results.

Each of the above should contain **specifics** about your data analyses (e.g. concrete numbers). The code you used to obtain your results should be included in your notebook, **below the Summary of Findings** section.

### Style

When doing the work that informs your summary, **you should write organized, readable code, broken into clearly separated sections.**

* Your work for each of the three project sections (Cleaning and EDA, Assessment of Missingness, and Hypothesis Testing) described below should be completed in code cells underneath the Markdown header of that section's name.
* You should **only include work that is relevant** to posing, explaining, and answering the question(s) you stated in the summary. You should include data quality, cleaning, and missingness assessments, though these should broadly be relevant to the question at hand.
* Do **not** include long DataFrame output; if you want to include specific data from a DataFrame in the writeup, display only the `head`.
* Make sure to clearly explain what each component of your notebook **means**. Specifically:
    - All plots should have titles.
    - All code cells should containing a comment describing how the code works.
    - All code cells and plots should have a Markdown cell preceeding them describing how the code/plot is related to your analysis. 

### Requirement: Cleaning and EDA (Exploratory Data Analysis)

* **Data Cleaning:** Clean the data appropriately for your question. For instance, you may need to replace data that should be missing with `NaN` or create new columns out of given ones (e.g. compute distances, scale data, or get time information from time stamps).
* **Univariate Analysis:** Look at the distributions of relevant columns separately by using DataFrame operations and drawing appropriate plots.
* **Bivariate Analysis:** Look at the statistics of pairs of columns to identify possible associations. For instance, you may create scatter plots and plot conditional distributions, or box-plots. Also, create pivot tables. These will be heloful in identifying interesting hypothesis tests!
* **Interesting Aggregates:** Choose columns to groupby and examine aggregate statistics.

### Requirement: Assessment of Missingness

* Recall, to determine whether data are likely NMAR, you must reason about the data generating process; you cannot conclude that data are likely NMAR solely by looking at your data. In your summary, **address whether you believe there is a column in your dataset that is NMAR**. Explain your reasoning and any additional data you might want to obtain that could explain the missingness (thereby making it MAR).
* In this section, you will **try and determine if values in a column are MAR dependent on some other column**. To do so:
    * Pick a column with non-trivial missingness to analyze.
    * Perform permutation tests to analyze the dependency of the missingness of this column on other columns.
        - Find at least one other column that the missingness of your selected column depends on, and one other column that the missingness of your selected column does not depend on.
            - _For the Stock Trades dataset, you instead will have to show three cases where the missingness of the data is dependent on another column. If you work with this dataset, you should notice that there is only a single column with non-trivial missingness, and you should verify yourself that the missingness of that column depends on most other columns._
    * Interpret the results of your permutation tests with respect to your data and question.

### Requirement: Hypothesis Testing

* Formulate a pair of hypotheses and perform a **hypothesis test or a permutation test** (that is not related to missingness). You can use the "sample questions" in each of the dataset descriptions for inspiration, or you can create your own.
* Be sure to explicitly state your null and alternative hypotheses, your choice of test statistic and significance level, the resulting p-value, and your conclusion. Justify why these choices are good choices for answering the question you are trying to answer.

---

## Dataset Descriptions
Below this section you will find descriptions for the three datasets you can choose from. In each of the descriptions you will be given additional information, such as:
* Steps on how to access the data.
* Sample questions you can investigate for your hypothesis test.
* Guidelines on how you can go about cleaning the data and performing EDA.
* What missingness you should look for in the dataset.

When selecting which dataset you are going to use for your project, try choosing the one whose topic appeals to you the most as that will make finishing the project a lot more enjoyable. Furthermore, **Project 5 will also be an open-ended project and will require you to choose one of the same three datasets. We recommend that you choose the same dataset in both Project 3 and Project 5**, so that you don't have to relearn a new dataset for Project 5.

---

## NYPD Civilian Complaints 🚔
This dataset contains data on 12,000 civilian complaints filed against New York City police officers.

### Getting the Data
{:.no_toc}

The data and its corresponding data dictionary are downloadable [here](https://www.propublica.org/datastore/dataset/civilian-complaints-against-new-york-city-police-officers).

***Note:*** You don't need to provide any information to obtain the data. Just agree to the terms of use and click "submit."

### Sample Questions
{:.no_toc}

- Does the length that the complaint is open depend on ethnicity/age/gender?
- Are white officer vs. non-white complainant cases more likely to go against the complainant? 
- Are allegations more severe for cases in which the officer and complainant are not of the same ethnicity?
- Are the complaints of women more successful than men (for the same allegations?)

There are a lot of other questions that can be asked from this data, so be creative! You are not limited to the sample questions above.

### Cleaning and EDA
{:.no_toc}

Follow all of the steps in the [Requirement: Cleaning and EDA](#requirement-cleaning-and-eda-exploratory-data-analysis) section. Note:

- Certain fields have "missing" data that isn't labeled as missing. For example, there are fields with the value "Unknown." Do some exploration to find those values and convert them to null values.
- You may also want to combine the date columns to create a column of type `pd.Timestamp` for time series exploration.

### Assessment of Missingness
{:.no_toc}

Follow all of the steps in the [Requirement: Assessment of Missingness](#requirement-assessment-of-missingness) section.

### Hypothesis Testing
{:.no_toc}

Follow all of the steps in the [Requirement: Hypothesis Testing](#requirement-hypothesis-testing) section. You can use the sample questions for inspiration.

---

## Power Outages 🔋
This dataset has major power outage data in the continental U.S. from January 2000 to July 2016.

### Getting the Data
{:.no_toc}

The data is downloadable [here](https://engineering.purdue.edu/LASCI/research-data/outages/outagerisks).

Note: If you are having a hard time with the "This dataset" link, hold shift and click the link to open it into a new tab and then refresh that new tab.

A data dictionary is available at this [article](https://www.sciencedirect.com/science/article/pii/S2352340918307182) under *Table 1. Variable descriptions*.


### Sample Questions
{:.no_toc}

- Where and when do major power outages tend to occur?
- What are the characteristics of major power outages with higher severity? Variables to consider include location, time, climate, land-use characteristics, electricity consumption patterns, economic characteristics, etc. What risk factors may an energy company want to look into when predicting the location and severity of its next major power outage?
- What characteristics are associated with each category of cause?
- How have characteristics of major power outages changed over time? Is there a clear trend?

### Cleaning and EDA
{:.no_toc}

Follow all of the steps in the [Requirement: Cleaning and EDA](#requirement-cleaning-and-eda-exploratory-data-analysis) section. Note:
- The data is given as an Excel file rather than a CSV. Open the data in Google Sheets or another spreadsheet application and determine which rows and columns of the sheet should be ignored when loading the data in `pandas`.
    - Note that `pandas` can load multiple filetypes: `pd.read_csv`, `pd.read_excel`, `pd.read_html`, `pd.read_json`, etc.
- The power outage start date and time is given by `'OUTAGE.START.DATE'` and `'OUTAGE.START.TIME'`. It would be preferable if these two columns were combined into one `pd.Timestamp` column. Combine `'OUTAGE.START.DATE'` and `'OUTAGE.START.TIME'` into a new `pd.Timestamp` column called `'OUTAGE.START'`. Similarly, combine `'OUTAGE.RESTORATION.DATE'` and `'OUTAGE.RESTORATION.TIME'` into a new `pd.Timestamp` column called `'OUTAGE.RESTORATION'`.
    - `pd.to_datetime` and `pd.to_timedelta` will be useful here.
- Tip: To visualize geospatial data, consider [Folium](https://python-visualization.github.io/folium/) or another geospatial plotting library.

### Assessment of Missingness
{:.no_toc}

Follow all of the steps in the [Requirement: Assessment of Missingness](#requirement-assessment-of-missingness) section.

### Hypothesis Test
{:.no_toc}

Follow all of the steps in the [Requirement: Hypothesis Testing](#requirement-hypothesis-testing) section. You can use the sample questions for inspiration.

---

## Stock Trades by Members of the US House of Representatives 📈

This project uses public data about the stock trades made by members of the US House of Representatives. This data is collected and maintained by Timothy Carambat as part of the [House Stock Watcher](https://housestockwatcher.com/) project. The project describes itself as follows:

> With recent and ongoing investigations of incumbent congressional members being investigated for potentially violating the STOCK act. This website compiles this publicly available information in a format that is easier to digest then the original `PDF` source.
>
> Members of Congress must report periodic reports of their asset transactions. This website is purely for an informative purpose and aid in transparency.
>
> This site does not manipulate or censor any of the information from the original source. All data is transcribed by our community of contributors, which you can join for free by going to our transcription tool. Our moderation team takes great care in ensuring the accuracy of the information.
>
> This site is built and maintained by Timothy Carambat and supported with our contributors.

### Getting the Data
{:.no_toc}

The full data set of stock trade disclosures is available as a CSV or as JSON at [this site](https://housestockwatcher.com/api). Note that the table at the top of the page, with columns `'Name of File'` and `'File Type'`, has a third column with download links that you may have to scroll to the right to see. You don't need to follow any of the API access instructions to download the data, you just need to click one of these links.

This data set does not, however, contain the political affiliation of the congresspeople. If you wish to investigate a question that relies on having this information, you'll need to find another dataset that contains it and perform a merge. ***Hint:*** Kaggle is a useful source of datasets.

### Sample Questions
{:.no_toc}

- Is there a difference in stock trading behavior between political parties? For example:
    - Does one party trade more often?
    - Does one party make larger trades?
    - Do the two parties invest in different stocks or sectors? For instance, do Democrats invest in Tesla more than Republicans?
- What congresspeople have made the most trades?
- What companies are most traded by congresspeople?
- Is there evidence of insider trading? For example, Boeing stock dropped sharply in February 2020. Were there a suspiciously-high number of sales of Boeing before the drop?
- When are stocks bought and sold? Is there a day of the week that is most common? Or a month of the year?


### Cleaning and EDA
{:.no_toc}

Follow all of the steps in the [Requirement: Cleaning and EDA](#requirement-cleaning-and-eda-exploratory-data-analysis) section. Note:

- Certain fields have "missing" data that isn't labeled as missing. For example, there are fields with the value `'--'`. Do some exploration to find those values and convert them to null values.
- You may also want to clean up the date columns to enable time series exploration.

### Assessment of Missingness
{:.no_toc}

Follow all of the steps in the [Requirement: Assessment of Missingness](#requirement-assessment-of-missingness) section.

***Note:*** Remember that the missingness requirements for this dataset are different than the missingness requirements for the other two datasets.

### Hypothesis Testing
{:.no_toc}

Follow all of the steps in the [Requirement: Hypothesis Testing](#requirement-hypothesis-testing) section. You can use the sample questions for inspiration.


---

## Rubric and Submission

Your project will be graded out of 100 points. The rough rubric is shown below. If you satisfy these requirements, you will receive full credit.

| Component | Weight |
| --- | --- |
| Provided an introduction to the dataset and the analyses | 10 points |
| Cleaned data | 10 points |
| Performed univariate analyses | 10 points |
| Performed bivariate analyses and aggregation | 10 points |
| Addressed NMAR question | 5 points|
| Performed permutation tests for missingness | 10 points|
| Interpreted missingness test results | 10 points|
| Selected relevant columns for a hypothesis or permutation test | 5 points|
| Explicitly stated a null hypothesis | 5 points|
| Explicitly stated an alternative hypothesis | 5 points|
| Performed a hypothesis or permutation test | 10 points|
| Used a valid test statistic | 5 points|
| Computed a p-value and made a decision | 5 points|
| **Total** | **100 points**|

To submit the project, generate a **PDF of your Jupyter Notebook** that contains all of the requirements above, and upload that PDF to Gradescope. You will not need to upload the raw notebook to Gradescope.

To export your notebook as a PDF, go to "File > Download as > HTML (.html)". Then, open the `.html` file that was created, and save a print preview of that webpage as a PDF. There are other ways to save a notebook as a PDF but they may require that you have additional packages installed on your computer, so this is likely the most straightforward.

There are three "Project 3" assignments on Gradescope, one for each dataset. Make sure to submit to the correct one, and to tag your partner!

---
