# Generated by Django 4.1.2 on 2022-11-19 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0008_aula_aluno'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacote',
            name='duracao_aula',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
