# Generated by Django 2.2.17 on 2021-02-01 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emanuel', '0004_auto_20210131_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prova',
            old_name='gabarito',
            new_name='prova',
        ),
    ]