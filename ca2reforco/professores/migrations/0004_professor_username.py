# Generated by Django 4.1.2 on 2022-11-03 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professores', '0003_alter_professor_data_nascimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
