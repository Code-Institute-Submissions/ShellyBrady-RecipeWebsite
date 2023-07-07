from django.apps import AppConfig
from django.db.models.signals import pre_save


class RecipesiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipesite'


def ready(self):
    from .models import Submission, submission_slug
    pre_save.connect(submission_slug, sender=Submission)
