# Generated by Django 3.2.18 on 2023-07-12 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipesite', '0050_comment_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='approved',
        ),
    ]