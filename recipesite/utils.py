from django.utils.text import slugify
from .models import Submission


def update_submission_slugs():
    submissions = Submission.objects.all()

    for submission in submissions:
        if submission.slug == 'default-slug':
            submission.slug = slugify(submission.title)

        submission.save()
