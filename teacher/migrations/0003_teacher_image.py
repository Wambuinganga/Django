# Generated by Django 2.2.1 on 2019-07-26 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20190531_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, upload_to='teacher_image'),
        ),
    ]
