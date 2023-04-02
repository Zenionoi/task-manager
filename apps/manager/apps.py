from django.apps import AppConfig


class MyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = 'apps.manager'
    label = 'apps_manager'
