# Generated by Django 5.0.6 on 2024-05-25 14:21

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_author_alter_article_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.IntegerField(verbose_name=django.contrib.auth.models.User),
        ),
    ]