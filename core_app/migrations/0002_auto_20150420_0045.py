# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
import django.core.validators



class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0001_initial'),
    ]



    operations = [

        migrations.CreateModel(
            name='AlarmaReportada',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=255)),
                ('descripcion', models.CharField(default='', max_length=512)),
                ('fecha_hora', models.DateTimeField(verbose_name=datetime.datetime(2015, 4, 16, 6, 35, 15, 725766))),
                ('nivel_alerta', models.IntegerField(default=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('alarma', models.ForeignKey(to='core_app.Alarma')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='alarmareportada',
            name='leida',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alarmareportada',
            name='fecha_hora',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 4, 20, 0, 45, 45, 221159)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_hora_evento',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 4, 20, 0, 45, 45, 217169)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_hora_sistema',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 4, 20, 0, 45, 45, 217221)),
            preserve_default=True,
        ),
    ]
