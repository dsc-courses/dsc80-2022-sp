# lab.py


import os
import pandas as pd
import numpy as np
from scipy import stats


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------



def first_round():
    """
    :return: list with two values as described in the notebook
    >>> out = first_round()
    >>> isinstance(out, list)
    True
    >>> out[0] < 1
    True
    >>> out[1] in ['NR', 'R']
    True
    """
    ...


def second_round():
    """
    :return: list with three values as described in the notebook
    >>> out = second_round()
    >>> isinstance(out, list)
    True
    >>> out[0] < 1
    True
    >>> out[1] in ['NR', 'R']
    True
    >>> out[2] in ['ND', 'D']
    True
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def verify_child(heights):
    """
    Returns a Series of p-values assessing the missingness
    of child-height columns on father height.
    
    :Example:
    >>> heights_fp = os.path.join('data', 'missing_heights.csv')
    >>> heights = pd.read_csv(heights_fp)
    >>> out = verify_child(heights)
    >>> out['child_50'] < out['child_95']
    True
    >>> out['child_5'] > out['child_50']
    True
    """
    ...


def missing_data_amounts():
    """
    Returns a list of multiple choice answers.
    :Example:
    >>> set(missing_data_amounts()) <= set(range(1, 6))
    True
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def cond_single_imputation(new_heights):
    """
    cond_single_imputation takes in a DataFrame with columns 
    father and child (with missing values in child) and imputes 
    single-valued mean imputation of the child column, 
    conditional on father. Your function should return a Series.

    :Example:
    >>> heights_fp = os.path.join('data', 'missing_heights.csv')
    >>> new_heights = pd.read_csv(heights_fp)[['father', 'child_50']]
    >>> new_heights = new_heights.rename(columns={'child_50': 'child'})
    >>> out = cond_single_imputation(new_heights)
    >>> out.isna().sum() == 0
    True
    >>> (new_heights['child'].std() - out.std()) > 0.5
    True
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def quantitative_distribution(child, N):
    """
    quantitative_distribution that takes in a Series and an integer 
    N > 0, and returns an array of N samples from the distribution of 
    values of the Series as described in the question.
    :Example:
    >>> heights_fp = os.path.join('data', 'missing_heights.csv')
    >>> heights = pd.read_csv(heights_fp)
    >>> child = heights['child_50']
    >>> out = quantitative_distribution(child, 100)
    >>> out.min() >= 56
    True
    >>> out.max() <= 79
    True
    >>> np.isclose(out.mean(), child.mean(), atol=1)
    True
    >>> np.isclose(out.std(), 3.5, atol=0.65)
    True
    """
    ...


def impute_height_quant(child):
    """
    impute_height_quant takes in a Series of child heights 
    with missing values and imputes them using the scheme in
    the question.
    :Example:
    >>> heights_fp = os.path.join('data', 'missing_heights.csv')
    >>> heights = pd.read_csv(heights_fp)
    >>> child = heights['child_50']
    >>> out = impute_height_quant(child)
    >>> out.isna().sum() == 0
    True
    >>> np.isclose(out.mean(), child.mean(), atol=0.5)
    True
    >>> np.isclose(out.mean(), child.mean(), atol=0.2)
    True
    >>> np.isclose(out.std(), child.std(), atol=0.15)
    True
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def answers():
    """
    Returns two lists with your answers
    :return: Two lists: one with your answers to multiple choice questions
    and the second list has 6 websites that satisfy given requirements.
    >>> mc_answers, websites = answers()
    >>> len(mc_answers)
    4
    >>> len(websites)
    6
    """
    ...
