# Generated by Django 4.1.7 on 2023-04-16 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='last_cleaned_date',
            field=models.DateTimeField(null=True),
        ),
    ]
