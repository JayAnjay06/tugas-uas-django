# Generated by Django 4.1.4 on 2022-12-28 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_blog_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='media',
        ),
    ]
