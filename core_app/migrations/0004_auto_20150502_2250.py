# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0003_auto_20150428_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='embebido',
            field=models.CharField(max_length=1023, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alarmareportada',
            name='fecha_hora',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 5, 2, 22, 50, 53, 113224)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_hora_evento',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 5, 2, 22, 50, 53, 108634)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_hora_sistema',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 5, 2, 22, 50, 53, 108669)),
            preserve_default=True,
        ),
    ]
