# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-24 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votos', '0005_candidato_cantidad_de_votos_nulos'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='porcentaje_nulos',
            field=models.IntegerField(default=0, verbose_name='Porcentaje de nulos'),
        ),
    ]
