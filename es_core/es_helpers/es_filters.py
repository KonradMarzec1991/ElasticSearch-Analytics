from elasticsearch_dsl.query import (
    Match,
    Bool,
    Range
)

from es_core.es_helpers.es_search import BaseSearch
from es_core.utils import execute_query


@execute_query
def filter_by_fn(first_name):
    qs = BaseSearch().search()
    q = Match(FirstName=first_name)
    return qs.query(q)


@execute_query
def filter_by_ln(last_name):
    qs = BaseSearch().search()
    q = Match(LastName=last_name)
    return qs.query(q)


@execute_query
def filter_by_age(age: int):
    qs = BaseSearch().search()
    q = Bool(Range('greater_than', gte=age))
    return qs.query(q)
