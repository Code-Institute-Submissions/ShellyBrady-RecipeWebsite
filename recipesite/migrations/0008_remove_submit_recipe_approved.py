# Generated by Django 3.2.18 on 2023-03-08 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipesite', '0007_submit_recipe_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submit_recipe',
            name='approved',
        ),
    ]
