# Generated by Django 4.0.3 on 2022-03-18 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_alter_recipe_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='category',
        ),
    ]
