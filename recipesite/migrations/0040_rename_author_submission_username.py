# Generated by Django 3.2.18 on 2023-06-17 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipesite', '0039_alter_submission_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='author',
            new_name='username',
        ),
    ]