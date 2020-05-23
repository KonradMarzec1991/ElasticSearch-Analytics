"""
Helper functions for filters and aggregations
"""


def execute_query(func):
    def wrapper(*args, **kwargs):
        base_search = func(*args, **kwargs)
        return base_search.execute().hits.hits
    return wrapper


def execute_aggs(func):
    def wrapper(*args, **kwargs):
        base_search = func(*args, **kwargs)
        return base_search.execute()['aggregations']
    return wrapper


def create_range_buckets(start, end, step):
    ranges = []
    for v in range(start, end, step):
        ranges.append(
            {'from': start, 'to': start + step}
        )
    ranges.insert(0, {'to': start})
    ranges.append({'from': end})
    return ranges

