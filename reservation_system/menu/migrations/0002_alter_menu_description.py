# Generated by Django 3.2.16 on 2023-01-25 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
