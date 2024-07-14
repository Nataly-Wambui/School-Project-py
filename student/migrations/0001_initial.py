# Generated by Django 4.2.14 on 2024-07-11 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('code', models.PositiveSmallIntegerField()),
                ('age', models.PositiveIntegerField()),
                ('gender', models.PositiveSmallIntegerField()),
                ('classes', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=20)),
            ],
        ),
    ]
