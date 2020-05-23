from elasticsearch_dsl.query import Match

from es_core.es_base_search import BaseSearch
from es_core.utils import execute_query


@execute_query
def filter_by_fn(first_name):
    qs = BaseSearch().search()
    q = Match(FirstName=first_name)
    return qs.query(q)


print(filter_by_fn('ELVA'))