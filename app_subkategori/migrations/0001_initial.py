# Generated by Django 4.2.6 on 2023-11-15 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subkategori',
            fields=[
                ('id_subkategori', models.AutoField(primary_key=True, serialize=False)),
                ('id_kategori', models.CharField(max_length=100)),
                ('nama_subkategori', models.CharField(max_length=100)),
            ],
        ),
    ]
