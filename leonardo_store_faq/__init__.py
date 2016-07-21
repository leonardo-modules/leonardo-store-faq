
from django.apps import AppConfig

default_app_config = 'leonardo_store_faq.Config'


LEONARDO_APPS = ['leonardo_store_faq']


class Config(AppConfig):
    name = 'leonardo_store_faq'
    verbose_name = "leonardo-store-faq"
