# Generated by Django 4.2.14 on 2024-08-20 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(blank=True, related_name='courses', to='teacher.teacher'),
        ),
    ]
