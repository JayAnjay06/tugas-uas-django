# Generated by Django 4.1.4 on 2022-12-23 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AlterField(
            model_name='blog',
            name='images',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]