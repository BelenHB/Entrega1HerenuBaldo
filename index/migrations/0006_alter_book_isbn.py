# Generated by Django 4.0.3 on 2022-03-17 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_alter_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
