# Generated by Django 3.0.7 on 2020-06-30 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0002_goallog'),
    ]

    operations = [
        migrations.AddField(
            model_name='goallog',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]