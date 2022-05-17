# lab.py


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.preprocessing import Binarizer, QuantileTransformer, FunctionTransformer

import warnings
warnings.filterwarnings('ignore')


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def best_transformation():
    """
    Returns an integer corresponding to the correct option.

    :Example:
    >>> best_transformation() in [1, 2, 3, 4]
    True
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------



def create_ordinal(df):
    """
    create_ordinal takes in diamonds and returns a DataFrame of ordinal
    features with names ordinal_<col> where <col> is the original
    categorical column name.

    :Example:
    >>> diamonds = pd.read_csv(os.path.join('data', 'diamonds.csv'))
    >>> out = create_ordinal(diamonds)
    >>> set(out.columns) == {'ordinal_cut', 'ordinal_clarity', 'ordinal_color'}
    True
    >>> np.unique(out['ordinal_cut']).tolist() == [0, 1, 2, 3, 4]
    True
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------




def create_one_hot(df):
    """
    create_one_hot takes in diamonds and returns a DataFrame of one-hot 
    encoded features with names one_hot_<col>_<val> where <col> is the 
    original categorical column name, and <val> is the value found in 
    the categorical column <col>.

    :Example:
    >>> diamonds = pd.read_csv(os.path.join('data', 'diamonds.csv'))
    >>> out = create_one_hot(diamonds)
    >>> out.shape == (53940, 20)
    True
    >>> out.columns.str.startswith('one_hot').all()
    True
    >>> out.isin([0, 1]).all().all()
    True
    """
    ...



def create_proportions(df):
    """
    create_proportions takes in diamonds and returns a 
    DataFrame of proportion-encoded features with names 
    proportion_<col> where <col> is the original 
    categorical column name.

    >>> diamonds = pd.read_csv(os.path.join('data', 'diamonds.csv'))
    >>> out = create_proportions(diamonds)
    >>> out.shape[1] == 3
    True
    >>> out.columns.str.startswith('proportion_').all()
    True
    >>> ((out >= 0) & (out <= 1)).all().all()
    True
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def create_quadratics(df):
    """
    create_quadratics that takes in diamonds and returns a DataFrame 
    of quadratic-encoded features <col1> * <col2> where <col1> and <col2> 
    are the original quantitative columns 
    (col1 and col2 should be distinct columns).

    :Example:
    >>> diamonds = pd.read_csv(os.path.join('data', 'diamonds.csv'))
    >>> out = create_quadratics(diamonds)
    >>> out.columns.str.contains(' * ').all()
    True
    >>> ('x * z' in out.columns) or ('z * x' in out.columns)
    True
    >>> out.shape[1] == 15
    True
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------



def comparing_performance():
    """
    Hard-coded answers to comparing_performance.
    :Example:
    >>> out = comparing_performance()
    >>> len(out) == 6
    True
    >>> import numbers
    >>> isinstance(out[0], numbers.Real)
    True
    >>> all(isinstance(x, str) for x in out[2:-1])
    True
    >>> out[1] > out[-1]
    True
    """

    # create a model per variable => (variable, R^2, RMSE) table
    ...


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


class TransformDiamonds(object):
    
    def __init__(self, diamonds):
        self.data = diamonds
        
    # Question 6.1
    def transform_carat(self, data):
        """
        transform_carat takes in a DataFrame like diamonds 
        and returns a binarized carat column (an np.ndarray).
        :Example:
        >>> diamonds = pd.read_csv(os.path.join('data', 'diamonds.csv'))
        >>> out = TransformDiamonds(diamonds)
        >>> transformed = out.transform_carat(diamonds)
        >>> isinstance(transformed, np.ndarray)
        True
        >>> transformed[172, 0] == 1
        True
        >>> transformed[0, 0] == 0
        True
        """
        ...
    
    # Question 6.2
    def transform_to_quantile(self, data):
        """
        transform_to_quantiles takes in a DataFrame like diamonds 
        and returns an np.ndarray of quantiles of the weight 
        (i.e. carats) of each diamond.
        :Example:
        >>> diamonds = pd.read_csv(os.path.join('data', 'diamonds.csv'))
        >>> out = TransformDiamonds(diamonds)
        >>> transformed = out.transform_to_quantile(diamonds)
        >>> isinstance(transformed, np.ndarray)
        True
        >>> np.isclose(transformed[0, 0], 0.0075757, atol=0.0001)
        True
        >>> np.isclose(transformed[1, 0], 0.0025252, atol=0.0001)
        True
        """
        ...
    
    # Question 6.3
    def transform_to_depth_pct(self, data):
        """
        transform_to_volume takes in a DataFrame like diamonds 
        and returns an np.ndarray consisting of the approximate 
        depth percentage of each diamond.
        :Example:
        >>> diamonds = pd.read_csv(os.path.join('data', 'diamonds.csv')).drop(columns='depth')
        >>> out = TransformDiamonds(diamonds)
        >>> transformed = out.transform_to_depth_pct(diamonds)
        >>> len(transformed.shape) == 1
        True
        >>> np.isclose(transformed[0], 61.286, atol=0.0001)
        True
        """
        ...
