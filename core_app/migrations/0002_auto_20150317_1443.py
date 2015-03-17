# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryAlarmas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=255, default='')),
                ('estado', models.BooleanField(default=True)),
                ('fecha', models.DateTimeField()),
                ('inmueble', models.ForeignKey(to='core_app.Inmueble')),
                ('parametro', models.ForeignKey(to='core_app.AlarmaParametro')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='evento',
            name='elemento',
            field=models.ForeignKey(to='core_app.Elemento', default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='evento',
            name='prioridad',
            field=models.CharField(max_length=1, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='tipoEven',
            field=models.CharField(max_length=2, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evento',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=True,
        ),
    ]
