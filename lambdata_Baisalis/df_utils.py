"""
utility function for working with Dataframes
"""

import pandas

TEST_DF = pandas.DataFrame([1,2,3])


def three_way_split(X):
    '''
    Perform train, test, val split on input dataframe
    '''
    train, test = train_test_split(X)
    train, val = train_test_split(train)
    return train, test, val

def add_to_df(X, lst, name):
    '''
    Add a list to a dataframe with a given column name. Input dataframe, list, name
    '''
    X[name] = lst
    return X
