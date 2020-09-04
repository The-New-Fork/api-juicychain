# Generated by Django 3.1 on 2020-09-03 16:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BatchesRefresco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('anfp', models.CharField(max_length=8)),
                ('dfp', models.CharField(max_length=40)),
                ('bnfp', models.CharField(max_length=10)),
                ('pds', models.DateField()),
                ('pde', models.DateField()),
                ('jds', models.IntegerField(blank=True, null=True)),
                ('jde', models.IntegerField(blank=True, null=True)),
                ('bbd', models.DateField()),
                ('pc', models.CharField(max_length=3)),
                ('pl', models.CharField(max_length=30)),
                ('rmn', models.CharField(max_length=20)),
                ('pon', models.CharField(max_length=10)),
                ('pop', models.CharField(max_length=3)),
            ],
        ),
    ]