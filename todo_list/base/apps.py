from django.apps import AppConfig

# spojenie app so server site 
class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
