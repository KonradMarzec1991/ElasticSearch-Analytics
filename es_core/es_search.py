"""
Basic set-up ElasticSearch search
"""

from django.conf import settings

from elasticsearch import Elasticsearch
from elasticsearch_dsl import (
    connections,
    Search
)


def get_client():
    """
    Basic ElasticSearch connection
    :return: connection client instance
    """
    return Elasticsearch(
        hosts={
            'host': settings.ES_HOST,
            'port': settings.ES_PORT
        }
    )


class BaseSearch:
    """
    Base search class for setting searches for different purposes
    """
    def __init__(self):
        self.es = connections.connections.create_connection(
            hosts=['localhost']
        )

    def search(self, index='employees'):
        return Search(using=self.es, index=index)

    def agg_search(self):
        """
        Search instance with addtional size equals 0
        :return: setup search instance
        """
        return self.search().extra(size=0)



