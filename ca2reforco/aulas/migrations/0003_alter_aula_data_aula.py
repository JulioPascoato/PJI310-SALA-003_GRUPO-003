# Generated by Django 4.1.2 on 2022-10-29 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0002_aula_data_aula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='data_aula',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]