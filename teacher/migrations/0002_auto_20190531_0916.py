# Generated by Django 2.2.1 on 2019-05-31 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='id_number',
            field=models.IntegerField(),
        ),
    ]
