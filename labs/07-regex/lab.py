# lab.py


import pandas as pd
import numpy as np
import os
import re


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def match_1(string):
    """
    Write a regular expression that matches strings that have
    '[' as the third character and 
    ']' as the sixth character.

    DO NOT EDIT THE DOCSTRING!
    >>> match_1("abcde]")
    False
    >>> match_1("ab[cde")
    False
    >>> match_1("a[cd]")
    False
    >>> match_1("ab[cd]")
    True
    >>> match_1("1ab[cd]")
    False
    >>> match_1("ab[cd]ef")
    True
    >>> match_1("1b[#d] _")
    True
    """
    pattern = ...

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_2(string):
    """
    Write a regular expression that matches strings that are phone numbers that 
    start with '(858)' and follow the format '(xxx) xxx-xxxx' ('x' represents a digit).
    Note: There is a space between '(xxx)' and 'xxx-xxxx'.
    
    DO NOT EDIT THE DOCSTRING!
    >>> match_2("(123) 456-7890")
    False
    >>> match_2("858-456-7890")
    False
    >>> match_2("(858)45-7890")
    False
    >>> match_2("(858) 456-7890")
    True
    >>> match_2("(858)456-789")
    False
    >>> match_2("(858)456-7890")
    False
    >>> match_2("a(858) 456-7890")
    False
    >>> match_2("(858) 456-7890b")
    False
    """
    pattern = ...

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_3(string):
    """
    Write a regular expression that matches strings that:
    - are between 6 and 10 characters long (inclusive),
    - contain only alphanumeric characters, whitespace and `'?'`, and
    - end with `'?'`.
    
    DO NOT EDIT THE DOCSTRING!
    >>> match_3("qwertsd?")
    True
    >>> match_3("qw?ertsd?")
    True
    >>> match_3("ab c?")
    False
    >>> match_3("ab   c ?")
    True
    >>> match_3(" asdfqwes ?")
    False
    >>> match_3(" adfqwes ?")
    True
    >>> match_3(" adf!qes ?")
    False
    >>> match_3(" adf!qe? ")
    False
    """
    pattern = ...

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_4(string):
    """
    Write a regular expression that matches strings with exactly two '$', 
    one of which is at the start of the string, such that:
    - the characters between the two '$' can be anything (including nothing) 
        except the lowercase letters 'a', 'b', and 'c', (and '$'), and
    - the characters after the second '$' can only be the lowercase or uppercase letters 
        'a'/'A', 'b'/'B', and 'c'/'C', with every 'a'/'A' before every 'b'/'B', 
        and every 'b'/'B' before every 'c'/'C'. 
        There must be at least one 'a' or 'A', at least one 'b' or 'B', and at least one 'c' or 'C'.
            
    DO NOT EDIT THE DOCSTRING!
    >>> match_4("$$AaaaaBbbbc")
    True
    >>> match_4("$!@#$aABc")
    True
    >>> match_4("$a$aABc")
    False
    >>> match_4("$iiuABc")
    False
    >>> match_4("123$$$Abc")
    False
    >>> match_4("$$Abc")
    True
    >>> match_4("$qw345t$AAAc")
    False
    >>> match_4("$s$Bca")
    False
    >>> match_4("$!@$")
    False
    """
    pattern = ...

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_5(string):
    """
    Write a regular expression that matches strings that represent valid 
    Python file names, including the extension.
    Note: For simplicity, assume that file names contains only letters, numbers, and underscores ('_').
    
    DO NOT EDIT THE DOCSTRING!
    >>> match_5("dsc80.py")
    True
    >>> match_5("dsc80py")
    False
    >>> match_5("dsc80..py")
    False
    >>> match_5("dsc80+.py")
    False
    """
    pattern = ...

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_6(string):
    """
    Write a regular expression that matches strings that:
    - are made up of only lowercase letters and exactly one underscore ('_'), and
    - have at least one lowercase letter on both sides of the underscore.
    
    DO NOT EDIT THE DOCSTRING!
    >>> match_6("aab_cbb_bc")
    False
    >>> match_6("aab_cbbbc")
    True
    >>> match_6("aab_Abbbc")
    False
    >>> match_6("abcdef")
    False
    >>> match_6("ABCDEF_ABCD")
    False
    """
    pattern = ...

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_7(string):
    """
    Write a regular expression that matches strings that start with and end with an underscore ('_').
    
    DO NOT EDIT THE DOCSTRING!
    >>> match_7("_abc_")
    True
    >>> match_7("abd")
    False
    >>> match_7("bcd")
    False
    >>> match_7("_ncde")
    False
    """
    pattern = ...

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None



def match_8(string):
    """
    Apple serial numbers are strings of length 1 or more that are 
    made up of any characters, other than
    - the uppercase letter `'O'`, 
    - the lowercase letter `'i`', and 
    - the number `'1'`.

    Write a regular expression that matches strings that are valid Apple serial numbers.
    
    DO NOT EDIT THE DOCSTRING!
    >>> match_8("ASJDKLFK10ASDO")
    False
    >>> match_8("ASJDKLFK0ASDo!!!!!!! !!!!!!!!!")
    True
    >>> match_8("JKLSDNM01IDKSL")
    False
    >>> match_8("ASDKJLdsi0SKLl")
    False
    >>> match_8("ASDJKL9380JKAL")
    True
    """
    pattern = ...

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None



def match_9(string):
    '''
    ID numbers are formatted as 'SC-NN-CCC-NNNN', where
    - SC represents state code in uppercase (e.g. 'CA'),
    - NN represents a number with 2 digits (e.g. '98'),
    - CCC represents a three letter city code in uppercase (e.g. 'SAN'), and
    - NNNN represents a number with 4 digits (e.g. '1024').
    Write a regular expression that matches strings that are ID numbers 
    corresponding to the cities of 'SAN' or 'LAX', or the state of 'NY'. 
    Assume that there is only one city named 'SAN', and only one city named 'LAX'.
    
    DO NOT EDIT THE DOCSTRING!
    >>> match_9('NY-32-NYC-1232')
    True
    >>> match_9('ca-23-SAN-1231')
    False
    >>> match_9('MA-36-BOS-5465')
    False
    >>> match_9('CA-56-LAX-7895')
    True
    >>> match_9('NY-32-LAX-0000') # If the state is NY, the city can be any 3 letter code
    True
    >>> match_9('TX-32-SAN-4491')
    False
    '''
    pattern = ...

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_10(string):
    '''
    Write a function named match_10 that takes in a string and:
    - converts the string to lowercase,
    - removes all non-alphanumeric characters (i.e. removes everything that is not in the \w character class), 
        and the letter 'a', and
    - returns a list of every non-overlapping three-character substring in the remaining string, 
        starting from the beginning of the string.


    See the notebook for more details.
    
    DO NOT EDIT THE DOCSTRING!
    >>> match_10('ABCdef')
    ['bcd']
    >>> match_10(' DEFaabc !g ')
    ['def', 'bcg']
    >>> match_10('Come ti chiami?')
    ['com', 'eti', 'chi']
    >>> match_10('and')
    []
    >>> match_10('Ab..DEF')
    ['bde']
    
    '''
    ...


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def extract_personal(s):
    """
    Extracts email addresses, Social Security Numbers, Bitcoin addresses and street addresses from input file
    :param s: file name as a string
    :return: a tuple of four separate lists
    
    :Example:
    >>> fp = os.path.join('data', 'messy.test.txt')
    >>> s = open(fp, encoding='utf8').read()
    >>> emails, ssn, bitcoin, addresses = extract_personal(s)
    >>> emails[0] == 'test@test.com'
    True
    >>> ssn[0] == '423-00-9575'
    True
    >>> bitcoin[0] == '1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2'
    True
    >>> addresses[0] == '530 High Street'
    True
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def tfidf_data(reviews_ser, review):
    """
    :Example:
    >>> fp = os.path.join('data', 'reviews.txt')
    >>> reviews_ser = pd.read_csv(fp, header=None, squeeze=True)
    >>> review = open(os.path.join('data', 'review.txt'), encoding='utf8').read().strip()
    >>> out = tfidf_data(reviews_ser, review)
    >>> out['cnt'].sum()
    85
    >>> 'before' in out.index
    True
    """
    ...


def relevant_word(out):
    """
    :Example:
    >>> fp = os.path.join('data', 'reviews.txt')
    >>> reviews_ser = pd.read_csv(fp, header=None, squeeze=True)
    >>> review = open(os.path.join('data', 'review.txt'), encoding='utf8').read().strip()
    >>> out = tfidf_data(reviews_ser, review)
    >>> relevant_word(out) in out.index
    True
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def hashtag_list(tweet_text):
    """
    :Example:
    >>> testdata = [['RT @DSC80: Text-cleaning is cool! #NLP https://t.co/xsfdw88d #NLP1 #NLP1']]
    >>> test = pd.DataFrame(testdata, columns=['text'])['text']
    >>> out = hashtag_list(test)
    >>> (out.iloc[0] == ['NLP', 'NLP1', 'NLP1'])
    True
    """
    ...


def most_common_hashtag(tweet_lists):
    """
    :Example:
    >>> testdata = [['RT @DSC80: Text-cleaning is cool! #NLP https://t.co/xsfdw88d #NLP1 #NLP1']]
    >>> test = hashtag_list(pd.DataFrame(testdata, columns=['text'])['text'])
    >>> most_common_hashtag(test).iloc[0] == 'NLP1'
    True
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------




    


def create_features(ira):
    """
    Takes in the ira data and returns a DataFrame with the described features.
    :param ira: the input DataFrame
    :return: a DataFrame with specified features
    
    :Example:
    >>> testdata = [['RT @DSC80: Text-cleaning is cool! #NLP https://t.co/xsfdw88d #NLP1 #NLP1']]
    >>> test = pd.DataFrame(testdata, columns=['text'])
    >>> out = create_features(test)
    >>> anscols = ['text', 'num_hashtags', 'mc_hashtags', 'num_tags', 'num_links', 'is_retweet']
    >>> ansdata = [['text cleaning is cool', 3, 'NLP1', 1, 1, True]]
    >>> ans = pd.DataFrame(ansdata, columns=anscols)
    >>> (out == ans).all().all()
    True
    """
    ...
