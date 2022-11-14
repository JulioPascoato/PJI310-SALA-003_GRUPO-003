from django.apps import AppConfig


class ProfessoresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'professores'

    def ready(self):
        import professores.signals
