# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-24 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votos', '0004_candidato_porcentaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='cantidad_de_votos_nulos',
            field=models.IntegerField(default=0, verbose_name='Cantidad de nulos'),
        ),
    ]
