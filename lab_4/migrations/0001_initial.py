# Generated by Django 2.1.1 on 2018-10-04 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sched',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=80)),
                ('tanggal', models.DateField()),
                ('jam', models.TimeField()),
                ('tempat', models.CharField(max_length=80)),
                ('kategori', models.CharField(max_length=80)),
            ],
        ),
    ]