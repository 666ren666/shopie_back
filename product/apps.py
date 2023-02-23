from django.apps import AppConfig


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'


class ShopperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shopper'
