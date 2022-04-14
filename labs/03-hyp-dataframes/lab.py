# lab.py


import os
import io
import pandas as pd
import numpy as np


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def car_null_hypoth():
    """
    Returns a list of valid null hypotheses.
    
    :Example:
    >>> set(car_null_hypoth()) <= set(range(1, 7))
    True
    """
    ...


def car_alt_hypoth():
    """
    Returns a list of valid alternative hypotheses.
    
    :Example:
    >>> set(car_alt_hypoth()) <= set(range(1, 7))
    True
    """
    ...

def car_test_stat():
    """
    Returns a list of valid test statistics.
    
    :Example:
    >>> set(car_test_stat()) <= set(range(1, 5))
    True
    """
    ...

def car_p_value():
    """
    Returns an integer corresponding to the correct explanation.
    
    :Example:
    >>> car_p_value() in set(range(1, 6))
    True
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def clean_universities(df):
    """ 
    clean_universities takes in the raw rankings DataFrame
    and returns a cleaned DataFrame according to the instructions
    in the lab notebook.
    >>> fp = os.path.join('data', 'universities_unified.csv')
    >>> df = pd.read_csv(fp)
    >>> cleaned = clean_universities(df)
    >>> cleaned.shape[0] == df.shape[0]
    True
    >>> cleaned['nation'].nunique() == 59
    True
    """
    ...

def university_info(cleaned):
    """
    university_info takes in a cleaned rankings DataFrame
    and returns a list containing the four values described
    in the lab notebook.
    >>> fp = os.path.join('data', 'universities_unified.csv')
    >>> df = pd.read_csv(fp)
    >>> cleaned = clean_universities(df)
    >>> info = university_info(cleaned)
    >>> len(info) == 4
    True
    >>> all([isinstance(x, y) for x, y in zip(info, [str, float, str, str])])
    True
    >>> info[2] in cleaned['state'].unique()
    True
    """
    ...



# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def std_scores_by_nation(cleaned):
    """
    std_scores_by_nation takes in a cleaned DataFrame of university rankings
    and returns a DataFrame containing standardized scores, according to
    the instructions in the lab notebook.
    >>> fp = os.path.join('data', 'universities_unified.csv')
    >>> play = pd.read_csv(fp)
    >>> cleaned = clean_universities(play)
    >>> out = std_scores_by_nation(cleaned)
    >>> out.shape[0] == cleaned.shape[0]
    True
    >>> set(out.columns) == set(['institution', 'nation', 'score'])
    True
    >>> np.all(abs(out.select_dtypes(include='number').mean()) < 10**-7)  # standard units should average to 0!
    True
    """
    ...
    

def su_and_spread():
    """
    >>> out = su_and_spread()
    >>> len(out) == 2
    True
    >>> out[0] in np.arange(1, 4)
    True
    >>> isinstance(out[1], str)
    True
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def read_linkedin_survey(dirname):
    """
    read_linkedin_survey combines all the survey*.csv files into a singular DataFrame
    :param dirname: directory name where the survey*.csv files are
    :returns: a DataFrame containing the combined survey data
    :Example:
    >>> dirname = os.path.join('data', 'responses')
    >>> out = read_linkedin_survey(dirname)
    >>> isinstance(out, pd.DataFrame)
    True
    >>> len(out)
    5000
    >>> read_linkedin_survey('nonexistentfile') # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    FileNotFoundError: ... 'nonexistentfile'
    """
    ...


def com_stats(df):
    """
    com_stats 
    :param df: a DataFrame containing the combined survey data
    :returns: a hardcoded list of answers to the problems in the notebook
    :Example:
    >>> dirname = os.path.join('data', 'responses')
    >>> df = read_linkedin_survey(dirname)
    >>> out = com_stats(df)
    >>> len(out)
    4
    >>> isinstance(out[0], int)
    True
    >>> isinstance(out[2], str)
    True
    """
    ...



# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def read_student_surveys(dirname):
    """
    read_student_surveys takes in a directory path 
    (containing files favorite*.csv) and combines 
    all of the survey data into one DataFrame, 
    indexed by student ID (a value 1-1000).

    :Example:
    >>> dirname = os.path.join('data', 'extra-credit-surveys')
    >>> out = read_student_surveys(dirname)
    >>> isinstance(out, pd.DataFrame)
    True
    >>> out.shape
    (1000, 6)
    >>> read_student_surveys('nonexistentfile') # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    FileNotFoundError: ... 'nonexistentfile'
    """
    ...


def check_credit(df):
    """
    check_credit takes in a DataFrame with the 
    combined survey data and outputs a DataFrame 
    of the names of students and how many extra credit 
    points they would receive, indexed by their ID (a value 1-1000).

    :Example:
    >>> dirname = os.path.join('data', 'extra-credit-surveys')
    >>> df = read_student_surveys(dirname)
    >>> out = check_credit(df)
    >>> out.shape
    (1000, 2)
    >>> out['ec'].max()
    6
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def most_popular_procedure(pets, procedure_history):
    """
    most popular 'ProcedureType'
    :Example:
    >>> pets_fp = os.path.join('data', 'pets', 'Pets.csv')
    >>> procedure_history_fp = os.path.join('data', 'pets', 'ProceduresHistory.csv')
    >>> pets = pd.read_csv(pets_fp)
    >>> procedure_history = pd.read_csv(procedure_history_fp)
    >>> out = most_popular_procedure(pets, procedure_history)
    >>> isinstance(out, str)
    True
    """
    ...

def pet_name_by_owner(owners, pets):
    """
    pet names by owner

    :Example:
    >>> owners_fp = os.path.join('data', 'pets', 'Owners.csv')
    >>> pets_fp = os.path.join('data', 'pets', 'Pets.csv')
    >>> owners = pd.read_csv(owners_fp)
    >>> pets = pd.read_csv(pets_fp)
    >>> out = pet_name_by_owner(owners, pets)
    >>> len(out) == len(owners)
    True
    >>> 'Sarah' in out.index
    True
    >>> 'Cookie' in out.values
    True
    """
    ...


def total_cost_per_city(owners, pets, procedure_history, procedure_detail):
    """
    total cost per city
​
    :Example:
    >>> owners_fp = os.path.join('data', 'pets', 'Owners.csv')
    >>> pets_fp = os.path.join('data', 'pets', 'Pets.csv')
    >>> procedure_detail_fp = os.path.join('data', 'pets', 'ProceduresDetails.csv')
    >>> procedure_history_fp = os.path.join('data', 'pets', 'ProceduresHistory.csv')
    >>> owners = pd.read_csv(owners_fp)
    >>> pets = pd.read_csv(pets_fp)
    >>> procedure_detail = pd.read_csv(procedure_detail_fp)
    >>> procedure_history = pd.read_csv(procedure_history_fp)
    >>> out = total_cost_per_city(owners, pets, procedure_history, procedure_detail)
    >>> set(out.index) <= set(owners['City'])
    True
    """
    ...
