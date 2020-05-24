"""
Helper functions for filters and aggregations
"""


allowed = ['Age', 'Designation', 'Gender', 'MaritalStatus', 'Salary']


def execute_query(func):
    def wrapper(*args):
        base_search = func(*args)
        return base_search.execute().hits.hits
    return wrapper


def execute_aggs(func):
    def wrapper(*args, **kwargs):
        base_search = func(*args, **kwargs)
        return base_search.execute()['aggregations']
    return wrapper


def check_term_field(func):
    def wrapper(arg):
        if arg not in allowed:
            raise ArgumentException
        return func(arg)
    return wrapper


class ArgumentException(Exception):
    pass


def create_range_buckets(start, end, step):
    ranges = []
    for v in range(start, end, step):
        ranges.append(
            {'from': start, 'to': start + step}
        )
    ranges.insert(0, {'to': start})
    ranges.append({'from': end})
    return ranges
