# Generated by Django 3.1.5 on 2021-01-28 17:16

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='audio_post',
            field=models.FileField(blank=True, upload_to=blog.models.get_file_path, verbose_name='Áudio do Post'),
        ),
    ]
