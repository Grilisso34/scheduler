# Generated by Django 3.2.18 on 2023-06-01 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surgeons', '0004_auto_20230601_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scheddepartures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.CharField(max_length=255, null=True)),
                ('tuesday', models.CharField(max_length=255, null=True)),
                ('wensday', models.CharField(max_length=255, null=True)),
                ('thursday', models.CharField(max_length=255, null=True)),
                ('friday', models.CharField(max_length=255, null=True)),
                ('surg', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='surgeons.surgeon')),
            ],
        ),
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=255, null=True)),
                ('day', models.CharField(max_length=255, null=True)),
                ('dutytype', models.CharField(max_length=255, null=True)),
                ('dutytime', models.CharField(max_length=255, null=True)),
                ('dayornight', models.CharField(max_length=255, null=True)),
                ('surg', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='surgeons.surgeon')),
            ],
        ),
    ]
