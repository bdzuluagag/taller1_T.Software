# Generated by Django 4.2 on 2023-05-17 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventofijo',
            name='fecha_creacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
