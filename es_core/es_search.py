"""
Basic set-up ElasticSearch search
"""


from elasticsearch_dsl import (
    connections,
    Search
)


class BaseSearch:
    def __init__(self):
        self.es = connections.connections.create_connection(
            hosts=['localhost']
        )

    def search(self, index='employees'):
        return Search(using=self.es, index=index)

    def agg_search(self, index='employees'):
        return self.search(using=self.es, index=index).extra(size=0)






