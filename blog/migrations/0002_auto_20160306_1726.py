# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='글쓴이',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='제목',
            new_name='title',
        ),
    ]
