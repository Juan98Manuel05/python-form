# Generated by Django 3.2.7 on 2021-09-14 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='date_hour_attention',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='requests',
            name='date_hour_attention_finish',
            field=models.DateTimeField(blank=True),
        ),
    ]
