# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_image', '0009_auto_20160713_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('filerimage_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, serialize=False, to='cmsplugin_filer_image.FilerImage')),
                ('card_title', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('cmsplugin_filer_image.filerimage',),
        ),
    ]
