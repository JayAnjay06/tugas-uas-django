# Generated by Django 4.1.4 on 2022-12-31 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_blog_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='images',
        ),
        migrations.AddField(
            model_name='blog',
            name='cover',
            field=models.ImageField(null=True, upload_to='cover/'),
        ),
    ]
