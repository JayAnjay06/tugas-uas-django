# Generated by Django 4.1.4 on 2022-12-23 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='images',
        ),
    ]