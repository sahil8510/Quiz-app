# Generated by Django 4.2.1 on 2023-05-26 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
