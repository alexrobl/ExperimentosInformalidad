# Generated by Django 3.1.13 on 2021-11-03 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experimentos', '0003_auto_20211102_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='set_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]