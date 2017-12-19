# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_image', '0009_auto_20160713_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Masthead',
            fields=[
                ('filerimage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, to='cmsplugin_filer_image.FilerImage', serialize=False)),
                ('masthead_name', models.CharField(max_length=50, verbose_name='name')),
                ('masthead_title', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('cmsplugin_filer_image.filerimage',),
        ),
    ]
