# discussion.py


import numpy as np
import pandas as pd
import os


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def hyp_test_lower_avg(df, N):
    """
    Tests whether the lower avg. of 'Go' is due to chance alone.
    
    - The function should take a DataFrame like prog_df, number of null test statistic simulations N,
    - It should return a list containing a) observed test statistic, b) and the p-value of the hypothesis test

    :Example:
    >>> prog_df = pd.read_csv(os.path.join('data','prog_df.csv'))
    >>> q1_out = hyp_test_lower_avg(prog_df, 1000)
    >>> isinstance(q1_out, list)
    True
    >>> np.isclose(q1_out[0], 76.96903195339905, atol=0.01)
    True
    >>> 0.08 <= q1_out[1] <= 0.20
    True
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def combined_seasons(df1, df2):
    """
    Create a function that return, as a tuple, a dataframe combining
    the 2017 and 2018 MLB seasons as well as the team that hit the most
    homeruns between the two seasons.

    :Example:
    >>> mlb_2017 = pd.read_csv(os.path.join('data','mlb_2017.txt'))
    >>> mlb_2018 = pd.read_csv(os.path.join('data','mlb_2018.txt'))
    >>> q2_out = combined_seasons(mlb_2017, mlb_2018)
    >>> q2_out[0].shape == (30, 56)
    True
    >>> q2_out[1] in q2_out[0].index
    True
    >>> all([(('_2017' in x) or ('_2018' in x)) for x in q2_out[0]])
    True
    >>> q2_out[1] == 'NYY'
    True
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def seasonal_average(df1, df2):
    """
    Combines df1 and df2 and take the mean of each column 
    for each team.
    
    - The dataframe you return should be indexed by team name (Tm).
    - Each column should contain the average value between the 2017 
    and 2018 seasons for the given statistic for each team.

    :Example:
    >>> mlb_2017 = pd.read_csv(os.path.join('data','mlb_2017.txt'))
    >>> mlb_2018 = pd.read_csv(os.path.join('data','mlb_2018.txt'))
    >>> q3_out = seasonal_average(mlb_2017, mlb_2018)
    >>> q3_out.shape == (30, 28)
    True
    >>> q3_out.index.nunique() == 30
    True
    >>> q3_out.loc['MIN']['HR'] == 186
    True
    >>> q3_out.loc['OAK'].max() == 6190.5
    True
    """
    ...
