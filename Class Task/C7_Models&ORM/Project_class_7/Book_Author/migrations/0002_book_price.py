# Generated by Django 4.2.11 on 2024-10-18 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book_Author', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
