# Generated by Django 3.1.13 on 2021-11-02 21:06

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('experimentos', '0002_auto_20211102_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='disclaimer',
            field=tinymce.models.HTMLField(verbose_name='Pegue aca su disclaimer y de estilos.'),
        ),
    ]
