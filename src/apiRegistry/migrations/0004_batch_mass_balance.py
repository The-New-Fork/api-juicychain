# Generated by Django 3.1.7 on 2021-06-17 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiRegistry', '0003_remove_batch_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='mass_balance',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]