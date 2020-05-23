from django.apps import AppConfig
from django.conf import settings
from elasticsearch_dsl.connections import connections


class EsCoreConfig(AppConfig):
    name = 'es_core'

    def ready(self):
        connections.configure(**settings.ES_CONNECTIONS)
