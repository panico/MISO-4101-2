# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0002_auto_20150317_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='id',
            field=models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False),
            preserve_default=True,
        ),
    ]
