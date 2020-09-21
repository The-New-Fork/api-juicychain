# Generated by Django 3.1 on 2020-09-21 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('raddress', models.CharField(blank=True, default='', max_length=34, null=True)),
                ('pubkey', models.CharField(blank=True, default='', max_length=66, null=True)),
                ('date_issue', models.DateField()),
                ('date_expiry', models.DateField()),
                ('issuer', models.CharField(max_length=128)),
                ('identifier', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raddress', models.CharField(editable=False, max_length=34, unique=True)),
                ('pubkey', models.CharField(editable=False, max_length=66, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PoolPurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raddress', models.CharField(editable=False, max_length=34, unique=True)),
                ('pubkey', models.CharField(editable=False, max_length=66, unique=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiRegistry.organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PoolBatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raddress', models.CharField(editable=False, max_length=34, unique=True)),
                ('pubkey', models.CharField(editable=False, max_length=66, unique=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiRegistry.organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raddress', models.CharField(editable=False, max_length=34, unique=True)),
                ('pubkey', models.CharField(editable=False, max_length=66, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='apiRegistry.organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CertificateRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raddress', models.CharField(editable=False, max_length=34, unique=True)),
                ('pubkey', models.CharField(editable=False, max_length=66, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('condition', models.CharField(max_length=255)),
                ('certificate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rule', to='apiRegistry.certificate')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='certificate',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificate', to='apiRegistry.organization'),
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raddress', models.CharField(editable=False, max_length=34, unique=True)),
                ('pubkey', models.CharField(editable=False, max_length=66, unique=True)),
                ('identifier', models.CharField(max_length=255)),
                ('date_production_start', models.DateField()),
                ('date_best_before', models.DateField()),
                ('origin_country', models.CharField(max_length=255)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiRegistry.organization')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
