# Generated by Django 4.2.14 on 2024-08-18 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course_details',
            field=models.ManyToManyField(to='course.course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=20),
        ),
    ]
