# Generated by Django 4.0.4 on 2022-04-20 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoas', '0003_alter_cliente_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPFCNPJ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=14, unique=True)),
            ],
        ),
    ]
