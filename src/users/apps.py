from django.apps import AppConfig


class TweetsConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals