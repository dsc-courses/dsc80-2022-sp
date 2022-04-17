# project.py


import numpy as np
import pandas as pd
import os


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def is_monotonic(arr):
    """
    Given a numpy array of numbers, determines if each entry is >= than the previous.
    
    Example
    -------
    
    >>> is_monotonic(np.array([3, 6, 2, 8]))
    False
    
    """
    ...


def monotonic_by_country(vacs):
    """
    Given a DataFrame like `vacs`, returns a DataFrame with one row for each country and 
    three bool columns - 'Doses_admin_monotonic', 'People_partially_vaccinated_monotonic', and 
    'People_fully_vaccinated_monotonic'. An entry in the 'Doses_admin' column should be True if the 
    country's Doses_admin is monotonically increasing and False otherwise; likewise for the other
    columns. The index of the returned DataFrame should contain country names.
    
    Example
    -------
    
    >>> # this file contains a subset of `vacs`
    >>> subset_vacs = pd.read_csv(os.path.join('data', 'covid-vaccinations-subset.csv'))
    >>> result = monotonic_by_country(subset_vacs)
    >>> isinstance(result, pd.DataFrame)
    True
    >>> result.shape == (2, 3)
    True
    >>> result.loc['Venezuela', 'Doses_admin_monotonic'] == False
    True
    
    """
    
    ...


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def robust_totals(vacs):
    """
    Accepts a DataFrame like vacs above and returns a DataFrame with one row for each 
    country/region and three columns - Doses_admin, People_partially_vaccinated, and 
    People_fully_vaccinated - where an entry in the Doses_admin column is the 97th 
    percentile of the values in that column for that country; likewise for the other 
    columns. The index of the returned DataFrame should contain country names.
    
    Example
    -------
    
    >>> # this file contains a subset of `vacs`
    >>> subset_vacs = pd.read_csv(os.path.join('data', 'covid-vaccinations-subset.csv'))
    >>> subset_tots = robust_totals(subset_vacs)
    >>> isinstance(subset_tots, pd.DataFrame)
    True
    >>> subset_tots.shape
    (2, 3)
    >>> int(subset_tots.loc['Venezuela', 'Doses_admin'])
    15714857
    
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def fix_dtypes(pops_raw):
    """
    Accepts a DataFrame like pops_raw above and returns a DataFrame with exactly
    the same columns and rows, but with the data types "fixed" to be appropriate
    for the data contained within. In addition, ensure that all missing values are
    represented by np.NaN. All percentages should be represented as decimals – e.g.,
    27% should be 0.27.
    
    Example
    -------
    
    >>> pops_raw = pd.read_csv(os.path.join('data', 'populations.csv'))
    >>> pops = fix_dtypes(pops_raw)
    >>> isinstance(pops, pd.DataFrame)
    True
    >>> pops.shape
    (235, 11)
    >>> pops.loc[pops['Country (or dependency)'] == 'Montserrat', 'Population (2020)'].iloc[0]
    4993
    
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def missing_in_pops(tots, pops):
    """
    Takes in two DataFrames, the first, like tots above, containing the total number of
    vaccinations per country, and the second like pops above, containing the
    population of each country. It should return a Python set of names that appear
    in tots but not in pops.
    
    Example
    -------
    >>> tots = pd.DataFrame({
    ...         'Doses_admin': [1, 2, 3],
    ...         'People_partially_vaccinated': [1, 2, 3],
    ...         'People_fully_vaccinated': [1, 2, 3]
    ...     },
    ...     index = ['China', 'Angola', 'Republic of Data Science']
    ... )
    >>> pops_raw = pd.read_csv(os.path.join('data', 'populations.csv'))
    >>> pops = fix_dtypes(pops_raw)
    >>> missing = missing_in_pops(tots, pops)
    >>> isinstance(missing, set)
    True
    >>> missing
    {'Republic of Data Science'}
    """
    ...

    
def fix_names(pops):
    """
    Accepts one argument - a DataFrame like pops – and returns a copy of pops, but with the 
    'Country (or dependency)' column changed so that all countries that appear in tots 
    also appear in the result, with a few exceptions listed in the notebook.
    
    Example
    -------
    
    >>> pops_raw = pd.read_csv(os.path.join('data', 'populations.csv'))
    >>> pops = fix_dtypes(pops_raw)
    >>> pops_fixed = fix_names(pops)
    >>> isinstance(pops_fixed, pd.DataFrame)
    True
    >>> pops_fixed.shape
    (235, 11)
    >>> 'Burma' in pops_fixed['Country (or dependency)'].values
    True
    >>> not 'Myanmar' in pops_fixed['Country (or dependency)'].values
    True
    
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def top_k_fully_vaccinated(tots, pops_fixed, k):
    """
    Accepts three arguments: a DataFrame like `tots`, a DataFrame like `pops_fixed`, 
    and an integer, `k`, and returns a Series of the $k$ top vaccination rates of any country, 
    sorted in descending order. For the purposes of this question, we define vaccination rate 
    to be the number of fully vaccinated individuals divided by the total population. 
    The index of the Series should be the country name, and the rates 
    should be decimal numbers between 0 and 1.
    
    Example
    -------
    
    >>> # this file contains a subset of `tots`
    >>> tots_sample = pd.read_csv(os.path.join('data', 'tots_sample_for_tests.csv')).set_index('Country_Region')
    >>> pops_raw = pd.read_csv(os.path.join('data', 'populations.csv'))
    >>> pops = fix_dtypes(pops_raw)
    >>> pops_fixed = fix_names(pops)
    >>> top_k_fully_vaccinated(tots_sample, pops_fixed, 3).index[2]
    'Oman'
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def clean_israel_data(df):
    """
    Accepts a DataFrame like israel_raw and returns a new DataFrame where the missing
    ages are replaced by np.NaNs and the 'Age' column's data type is float. Furthermore,
    the 'Vaccinated' and 'Severe Sickness' columns should be stored as bools. The shape
    of the returned DataFrame should be the same as israel_raw, and, as usual, your
    function should not modify the input argument.
    
    Example
    -------
    
    >>> # this file contains a subset of israel.csv
    >>> israel_raw = pd.read_csv(os.path.join('data', 'israel-subset.csv'))
    >>> result = clean_israel_data(israel_raw)
    >>> isinstance(result, pd.DataFrame)
    True
    >>> str(result.dtypes['Age'])
    'float64'
    
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def mcar_permutation_tests(df, n_permutations=100):
    """
    Accepts two arguments – a DataFrame like israel and a number n_permutations of
    permutations – and runs the two permutation tests described in the notebook. Your
    function should return a 2-tuple where the first entry is an array of the simulated test
    statistics for the first permutation test, and the second entry is an array of
    simulated test statistics for the second permutation test.
    
    Example
    -------
    
    >>> israel_raw = pd.read_csv(os.path.join('data', 'israel-subset.csv'))
    >>> israel = clean_israel_data(israel_raw)
    >>> res = mcar_permutation_tests(israel, n_permutations=3)
    >>> isinstance(res[0], np.ndarray) and isinstance(res[1], np.ndarray)
    True
    >>> len(res[0]) == len(res[1]) == 3 # because only 3 permutations
    True
    
    """
    ...
    
    
def missingness_type():
    """
    Returns a single integer corresponding to the option below that you think describes
    the type of missingess in this data:

        1. MCAR (Missing completely at random)
        2. MAR (Missing at random)
        3. NMAR (Not missing at random)
        4. Missing by design
        
    Example
    -------
    >>> missingness_type() in {1, 2, 3, 4}
    True
    
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 8
# ---------------------------------------------------------------------


def effectiveness(df):
    """
    Accepts a DataFrame like vax above, and returns the effectiveness of the
    vaccine against severe illness.
    
    Example
    -------
    
    >>> example_vax = pd.DataFrame({
    ...             'Age': [15, 20, 25, 30, 35, 40],
    ...             'Vaccinated': [True, True, True, False, False, False],
    ...             'Severe Sickness': [True, False, False, False, True, True]
    ...         })
    >>> effectiveness(example_vax)
    0.5
    
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 9
# ---------------------------------------------------------------------


AGE_GROUPS = [
    '12-15',
    '16-19',
    '20-29',
    '30-39',
    '40-49',
    '50-59',
    '60-69',
    '70-79',
    '80-89',
    '90-'
]

def stratified_effectiveness(df):
    """
    Accepts one argument - a DataFrame like vax – and returns the effectiveness of the
    vaccine within each of the age groups in AGE_GROUPS. The return value of the function
    should be a Series of the same length as AGE_GROUPS, with the index of the Series being
    age groups as strings.
    
    Example
    -------
    
    >>> # this file contains a subset of israel.csv
    >>> israel_raw = pd.read_csv(os.path.join('data', 'israel-subset.csv'))
    >>> vax_subset = clean_israel_data(israel_raw).dropna()
    >>> stratified_effectiveness(vax_subset).index[0]
    '12-15'
    >>> len(stratified_effectiveness(vax_subset))
    10
    
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 10
# ---------------------------------------------------------------------


def effectiveness_calculator(
    *,
    young_vaccinated_prop,
    old_vaccinated_prop,
    young_risk_vaccinated,
    young_risk_unvaccinated,
    old_risk_vaccinated,
    old_risk_unvaccinated
):
    """Given various vaccination probabilities, computes the effectiveness.
    
    See the notebook for full instructions.
    
    Example
    -------
    
    >>> test_eff = effectiveness_calculator(
    ...  young_vaccinated_prop=0.5,
    ...  old_vaccinated_prop=0.5,
    ...  young_risk_vaccinated=0.01,
    ...  young_risk_unvaccinated=0.20,
    ...  old_risk_vaccinated=0.01,
    ...  old_risk_unvaccinated=0.20
    ... )
    >>> test_eff['Overall'] == test_eff['Young'] == test_eff['Old'] == 0.95
    True
    
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 11
# ---------------------------------------------------------------------


def extreme_example():
    """
    Accepts no arguments and returns a dictionary whose keys are the arguments to 
    the function effectiveness_calculator. When your function is called and 
    the dictionary is passed to effectiveness_calculator, it should return an 
    'Overall' effectiveness that is negative and 'Young' and 'Old' effectivenesses
    that are both over 0.8.
    
    Example
    -------
    
    >>> isinstance(extreme_example(), dict)
    True
    >>> keys = {
    ... 'young_vaccinated_prop',
    ... 'old_vaccinated_prop',
    ... 'young_risk_vaccinated',
    ... 'young_risk_unvaccinated',
    ... 'old_risk_vaccinated',
    ... 'old_risk_unvaccinated',
    ... }
    >>> extreme_example().keys() == keys
    True
    """
    ...
