# Generated by Django 2.2.6 on 2019-11-14 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_status_segmentacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status_segmentacao',
            name='status_seg',
            field=models.CharField(choices=[('0', 'Erro'), ('1', 'Processando'), ('2', 'Consluído')], default='1', max_length=20),
        ),
    ]