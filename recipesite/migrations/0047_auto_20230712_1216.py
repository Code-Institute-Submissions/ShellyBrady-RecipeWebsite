# Generated by Django 3.2.18 on 2023-07-12 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipesite', '0046_auto_20230707_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='recipesite.recipe'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='submission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='recipesite.submission'),
        ),
    ]
