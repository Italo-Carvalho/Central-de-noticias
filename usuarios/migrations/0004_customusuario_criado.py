# Generated by Django 3.1.5 on 2021-02-06 00:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20210205_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusuario',
            name='criado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Criação'),
            preserve_default=False,
        ),
    ]
