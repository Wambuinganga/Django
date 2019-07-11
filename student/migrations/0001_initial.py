# Generated by Django 2.2.1 on 2019-05-30 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('registration_number', models.CharField(max_length=50)),
                ('place_of_residence', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('guardian_phone', models.CharField(max_length=50)),
                ('id_number', models.IntegerField()),
                ('date_joined', models.DateField()),
                ('courses', models.ManyToManyField(to='course.Course')),
            ],
        ),
    ]
