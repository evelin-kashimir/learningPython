# Generated by Django 4.0.4 on 2022-05-13 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoa', '0002_usuarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
