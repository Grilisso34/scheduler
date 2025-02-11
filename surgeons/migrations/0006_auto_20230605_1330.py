# Generated by Django 3.2.18 on 2023-06-05 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surgeons', '0005_duty_scheddepartures'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operationdate', models.DateTimeField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='duty',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='receptiondays',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='scheddepartures',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='surgeon',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='workschedule',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='surgeon',
            name='birdhday',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='surgeon',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
        migrations.AlterField(
            model_name='surgeon',
            name='title',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Имя'),
        ),
        migrations.CreateModel(
            name='PatientInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientname', models.CharField(max_length=255)),
                ('diagnosis', models.CharField(max_length=255)),
                ('chrronicdeseases', models.CharField(max_length=255)),
                ('transferredoperations', models.CharField(max_length=255)),
                ('medicalcontraindications', models.CharField(max_length=255)),
                ('oper', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='surgeons.operation')),
            ],
        ),
        migrations.AddField(
            model_name='operation',
            name='surg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='surgeons.surgeon'),
        ),
        migrations.CreateModel(
            name='OpeartionSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operationdate', models.DateTimeField()),
                ('oper', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='surgeons.operation')),
                ('surg', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='surgeons.surgeon')),
            ],
        ),
    ]
