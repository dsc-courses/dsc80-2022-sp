# discussion.py


import numpy as np
import pandas as pd
import os


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def question01(data, labels):
    """
    Returns a dataframe from the
    given data (a dictionary of lists),
    and list of labels.

    >>> data = {'column1': [0,3,5,6], 'column2': [1,3,2,4]}
    >>> labels = 'a b c d'.split()
    >>> out_q1 = question01(data, labels)
    >>> isinstance(out_q1, pd.DataFrame)
    True
    >>> out_q1.index.tolist() == labels
    True
    >>> out_q1.loc['c', 'column1'] == 5
    True
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def question02(ser):
    """
    Given a Pandas Series, outputs the
    positions (an index or array) of 
    entries of ser that are multiples of 3.
    
    >>> out1_q2 = question02(pd.Series([1, 3, 6, 9]))
    >>> out2_q2 = question02(pd.Series([3, 6, 1, 9]))
    >>> out1_q2.tolist() == [1, 2, 3]
    True
    >>> out2_q2.tolist() == [0, 1, 3]
    True
    """
    ...
