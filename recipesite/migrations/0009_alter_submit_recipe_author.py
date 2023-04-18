# Generated by Django 3.2.18 on 2023-03-08 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipesite', '0008_remove_submit_recipe_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submit_recipe',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submitter', to=settings.AUTH_USER_MODEL),
        ),
    ]
