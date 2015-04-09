# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alarmaestado',
            old_name='estado',
            new_name='estado_sensor',
        ),
        migrations.RemoveField(
            model_name='alarma',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='alarmareportada',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='historyalarmas',
            name='user',
        ),
        migrations.AddField(
            model_name='alarma',
            name='nivel_alarma',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)], default=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alarma',
            name='descripcion',
            field=models.CharField(max_length=512, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alarma',
            name='notifica',
            field=models.BooleanField(help_text='envia notificacion', default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alarmaacceso',
            name='hora_fin',
            field=models.TimeField(help_text='hh:mm:ss'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alarmaacceso',
            name='hora_inicio',
            field=models.TimeField(help_text='hh:mm:ss'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alarmaestado',
            name='hora_fin',
            field=models.TimeField(help_text='hh:mm:ss'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alarmaestado',
            name='hora_inicio',
            field=models.TimeField(help_text='hh:mm:ss'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alarmareportada',
            name='descripcion',
            field=models.CharField(max_length=512, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alarmareportada',
            name='fecha_hora',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 4, 9, 21, 1, 28, 627920)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_hora_evento',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 4, 9, 21, 1, 28, 624966)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_hora_sistema',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 4, 9, 21, 1, 28, 625005)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='sensor',
            field=models.ForeignKey(to='core_app.Sensor', default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sensor',
            name='tipo_sensor',
            field=models.ForeignKey(to='core_app.TipoSensor', default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tiposensor',
            name='descripcion',
            field=models.CharField(max_length=255, default=''),
            preserve_default=True,
        ),
    ]
