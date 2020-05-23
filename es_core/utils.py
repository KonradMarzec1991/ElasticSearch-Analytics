"""
Helper functions for filters and aggregations
"""


def execute_query(func):
    def wrapper(*args, **kwargs):
        base_search = func(*args, **kwargs)
        return base_search.execute().hits.hits
    return wrapper
