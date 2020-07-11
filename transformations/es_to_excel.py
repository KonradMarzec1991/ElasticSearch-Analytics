"""
Pandas setup and helper functions
"""
import pandas as pd
from pandas import json_normalize

columns_to_drop = ['_index', '_type', '_id', '_score']


def drop_prefix(self, prefix):
    """Remove prefix from columns"""
    self.columns = self.columns.str.lstrip(prefix)
    return self


def drop_suffix(self, suffix):
    """Remove suffix from columns"""
    self.columns = self.columns.str.rstrip(suffix)
    return self


# Add functions to pd
pd.core.frame.DataFrame.drop_prefix = drop_prefix
pd.core.frame.DataFrame.drop_suffix = drop_suffix


def normalize_es_output(es_output):
    df = json_normalize(es_output)
    df.drop(columns_to_drop, inplace=True, axis='columns')
    df.drop_suffix('_source.')

    df['Salary'] = df['Salary'].astype(int)
    df['DateOfJoining'] = pd.to_datetime(df['DateOfJoining'])

    df['FullName'] = df[['FirstName', 'LastName']]\
        .agg(' '.join, axis='columns').str.title()
    df.drop(['FirstName', 'LastName', "Address"], inplace=True, axis='columns')

    cols = df.columns.to_list()
    cols = cols[-2:] + cols[:-2]
    df = df[cols]

    df.sort_values('Salary', inplace=True)
    return df


