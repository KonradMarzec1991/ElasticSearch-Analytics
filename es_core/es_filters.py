"""
Basic ElasticSearch filters
"""
from elasticsearch_dsl.query import (
    Match,
    Bool,
    Range,
    Term,
    MatchAll,
    Q
)

from es_core.es_search import BaseSearch
from es_core.utils import execute_query
from django.conf import settings

FIELDS = [
    'FirstName',
    'LastName',
    'MaritalStatus',
    'Gender',
    'Salary',
    'Age',
    'Interests',
    'DateOfJoining',
    'Designation'
]


@execute_query
def get_by_id(emp_id):
    """Basic query"""
    qs = BaseSearch().search()
    q = Term(_id=emp_id)
    return qs.query(q)


@execute_query
def match_all():
    """Basic query"""
    return BaseSearch().search().extra(size=settings.ES_DEFAULT_SIZE).query(
        MatchAll()
    )


@execute_query
def filter_by_fn(first_name):
    """Basic query - filters by first name"""
    qs = BaseSearch().search()
    q = Match(FirstName=first_name)
    return qs.query(q)


@execute_query
def filter_by_ln(last_name):
    """Basic query - filters by last name"""
    qs = BaseSearch().search()
    q = Match(LastName=last_name)
    return qs.query(q)


@execute_query
def filter_by_age(age: int):
    """Basic query - filters by age"""
    qs = BaseSearch().search().extra(size=10000)
    q = Bool(Range('greater_than', gte=age))
    return qs.query(q)


@execute_query
def general_filter(**kwargs):
    """
    General filter uses kwargs to filter out query
    :param kwargs: names of columns in ElasticSearch - filters
    :return: query with filters
    """
    qs = BaseSearch().search()
    terms_list = []
    for key in kwargs.keys():
        if key in FIELDS and kwargs[key]:
            if key in ['FirstName', 'LastName', 'Age']:
                content = {key: kwargs[key]}
                terms_list.append(Match(**content))
            else:
                content = {f'{key}.keyword': {'value': kwargs[key]}}
                terms_list.append(Q('term', **content))
    q = Bool(filter=terms_list)
    return qs.query(q)
