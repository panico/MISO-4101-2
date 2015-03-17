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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nombre', models.CharField(default='', max_length=255)),
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
    ]
