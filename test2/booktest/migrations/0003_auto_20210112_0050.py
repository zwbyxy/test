# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_areainfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areainfo',
            name='atitle',
            field=models.CharField(verbose_name='区域名称(字段)', max_length=30),
        ),
    ]
