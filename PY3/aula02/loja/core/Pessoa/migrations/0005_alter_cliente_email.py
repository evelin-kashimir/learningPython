# Generated by Django 4.0.4 on 2022-05-13 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoa', '0004_alter_fornecedor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
