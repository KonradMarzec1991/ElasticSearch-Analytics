"""
Basic set statistics
"""
from es_core.es_search import BaseSearch
from es_core.utils import execute_aggs
from .utils import create_range_buckets


@execute_aggs
def term_aggs_by_field(field):
    qs = BaseSearch().agg_search()
    qs.aggs.bucket(
        name='agg', agg_type='terms', field=field, size=50,
        order={'_key': 'asc'}
    )
    return qs


@execute_aggs
def salary_by_age():
    qs = BaseSearch().agg_search()
    qs.aggs.bucket(
        name='agg', agg_type='terms', field='Age', size=50,
        order={'_key': 'asc'}
    ).metric('salary_by_age', 'avg', field='Salary')
    return qs


@execute_aggs
def salary_by_bucket_ages():
    qs = BaseSearch().agg_search()
    qs.aggs.bucket(
        name='salary_by_buckets_dist', agg_type='range',
        field='Age', ranges=create_range_buckets(20, 55, 5)
    ).metric('salary_by_age', 'avg', field='Salary')


result = salary_by_bucket_ages()
for item in result['agg']['buckets']:
    print(item['key'], item['salary_by_age']['value'])