from django.apps import AppConfig


class FundraiserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '_fundraiser'

    # def ready(self) -> None:
    #     import _fundraiser.signals
