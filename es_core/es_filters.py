from elasticsearch_dsl.query import (
    Match,
    Bool,
    Range,
    Term,
    MatchAll
)


from es_core.es_search import BaseSearch
from es_core.utils import execute_query
from django.conf import settings


@execute_query
def get_by_id(emp_id):
    qs = BaseSearch().search()
    q = Term(_id=emp_id)
    return qs.query(q)


@execute_query
def match_all():
    return BaseSearch().search().extra(size=settings.ES_DEFAULT_SIZE).query(
        MatchAll()
    )


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
