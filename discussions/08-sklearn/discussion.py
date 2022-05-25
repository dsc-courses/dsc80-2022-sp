# discussion.py


import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


from sklearn.base import BaseEstimator, TransformerMixin

class LowStdColumnDropper(BaseEstimator, TransformerMixin):
    '''
    Drops columns whose standard deviation is less than thresh.
    '''
    def __init__(self, thresh=0):
        self.thresh = thresh

    def fit(self, X, y=None):
        """
        ...
        """
        # self.columns_ = ...
        # return self
        
        ...

    def transform(self, X, y=None):
        """
        >>> data = pd.read_csv('data/cars.csv').select_dtypes('number')
        >>> lvd = LowStdColumnDropper(thresh=10)
        >>> out = lvd.fit_transform(data)
        >>> out.shape[0] == data.shape[0]
        True
        >>> out.shape[1] <= data.shape[1]
        True
        """
        ...
