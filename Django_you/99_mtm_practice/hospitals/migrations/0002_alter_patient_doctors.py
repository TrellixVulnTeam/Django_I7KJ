# Generated by Django 3.2.7 on 2021-10-20 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='doctors',
            field=models.ManyToManyField(related_name='patients', to='hospitals.Doctor'),
        ),
    ]