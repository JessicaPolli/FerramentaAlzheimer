# Generated by Django 2.2.6 on 2019-11-25 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191124_1519'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]