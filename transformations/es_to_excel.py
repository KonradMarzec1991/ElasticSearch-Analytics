"""
Pandas setup and helper functions
"""

import pandas as pd
from pandas import json_normalize


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

