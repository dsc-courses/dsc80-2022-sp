# discussion.py


import pandas as pd
import numpy as np
from glob import glob

from scipy.stats import linregress


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def rmse(datasets):
    """
    Return the RMSE of each of the datasets.

    >>> datasets = {k:pd.read_csv('data/dataset_%d.csv' % k) for k in range(7)}
    >>> out = rmse(datasets)
    >>> len(out) == 7
    True
    >>> isinstance(out, pd.Series)
    True
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def onehot_encoding(df, col='relationship'):
    """
    Return a DataFrame that contains the one-hot encoded features of the specified variable

    >>> ohe_out = onehot_encoding(pd.read_csv('data/adult.csv'), col='relationship')
    >>> isinstance(ohe_out, pd.DataFrame)
    True
    >>> ohe_out.shape == (48842, 5)
    True
    >>> set(ohe_out.columns) == {'Husband', 'Not-in-family', 'Own-child', 'Unmarried', 'Wife'}
    True
    """
    ...
