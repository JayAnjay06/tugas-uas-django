# Generated by Django 4.1.4 on 2022-12-25 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_blog_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='judul',
            new_name='nama_universitas',
        ),
    ]
