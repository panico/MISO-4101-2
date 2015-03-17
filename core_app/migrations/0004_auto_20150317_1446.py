# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0003_auto_20150317_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='elemento',
            field=models.ForeignKey(to='core_app.Elemento'),
            preserve_default=True,
        ),
    ]
