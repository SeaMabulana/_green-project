from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '_users'

    def ready(self) -> None:
        import _users.signals
