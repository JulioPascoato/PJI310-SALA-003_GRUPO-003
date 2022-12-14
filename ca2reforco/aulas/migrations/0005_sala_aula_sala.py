# Generated by Django 4.1.2 on 2022-11-02 15:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0004_pacote_aula_pacote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('nome', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='aula',
            name='sala',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='aulas.sala'),
        ),
    ]
