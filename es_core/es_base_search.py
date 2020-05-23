"""
Basic set-up ElasticSearch search
"""


from elasticsearch_dsl import (
    connections,
    Search
)


class BaseSearch:

    @staticmethod
    def search(index='employees'):
        es_instance = connections.connections.create_connection(
            hosts=['localhost']
        )
        return Search(using=es_instance, index=index)





