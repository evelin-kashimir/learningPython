# Generated by Django 4.0.4 on 2022-04-20 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoas', '0002_alter_cliente_email'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cliente',
            table='Cliente',
        ),
    ]