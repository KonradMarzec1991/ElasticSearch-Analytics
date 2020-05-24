"""
Basic set of statistics
"""


from es_core.es_helpers.es_search import BaseSearch
from es_core.utils import (
    execute_aggs,
    check_term_field
)
from es_core.utils import create_range_buckets


@execute_aggs
@check_term_field
def term_aggs_by_field(field: str) -> list:
    """
    Basic ElasticSearch term aggregation for allowed fields
    :param field: name of field
    :return: query results
    """
    qs = BaseSearch().agg_search()
    qs.aggs.bucket(
        name='agg', agg_type='terms', field=field, size=50,
        order={'_key': 'asc'}
    )
    return qs


@execute_aggs
def salary_by_age() -> dict:
    """
    Metric ElasticSearch aggregation for showing salary by age (integer)
    :return: query results for salary by age
    """
    qs = BaseSearch().agg_search()
    qs.aggs.bucket(
        name='agg', agg_type='terms', field='Age', size=50,
        order={'_key': 'asc'}
    ).metric('avg_salary', 'avg', field='Salary')
    return qs


@execute_aggs
def salary_by_bucket_ages(start: int, end: int, step: int) -> dict:
    """
    Metric ElasticSearch aggregation for showing salary by age buckets
    :param start: start of range
    :param end: end of range
    :param step: length of bucket
    :return: query result for given args
    """
    qs = BaseSearch().agg_search()
    qs.aggs.bucket(
        name='salary_by_buckets_dist', agg_type='range',
        field='Age', ranges=create_range_buckets(start, end, step)
    ).metric('avg_salary', 'avg', field='Salary')
    return qs


@execute_aggs
def salary_by_gender():
    """
    Metric aggregation shows salary by gender
    :return: query result for salary by gender
    """
    qs = BaseSearch().agg_search()
    qs.aggs.bucket(
        name='salary_by_gender', agg_type='terms', field='Gender'
    ).metric('avg_salary', 'avg', field='Salary')
    return qs


@execute_aggs
def salary_by_gender_age_buckets(start: int, end: int, step: int) -> dict:
    """
    Metric aggregation shows salary for age bucket
    :param start: start of range
    :param end: end of range
    :param step: length of bucket
    :return: query result showing salary for age buckets
    """
    qs = BaseSearch().agg_search()
    qs.aggs.bucket(
        name='salary_by_buckets_dist', agg_type='range',
        field='Age', ranges=create_range_buckets(start, end, step)
    ).bucket('get_gender', 'terms', field='Gender'
             ).metric('avg_salary', 'avg', field='Salary')
    return qs


@execute_aggs
def median_by_gender_age_buckets():
    """
    Median aggregation for salary, gender and age buckets
    :return: query result showing median for salary, gender and age buckets
    """
    qs = BaseSearch().agg_search()
    qs.aggs.bucket(
        name='median_by_buckets_dist', agg_type='range',
        field='Age', ranges=create_range_buckets(20, 55, 5)
    ).bucket('get_gender', 'terms', field='Gender'
             ).metric('avg_salary', 'percentiles', field='Salary',
                      percents=[50, 90]
                      )
    return qs
