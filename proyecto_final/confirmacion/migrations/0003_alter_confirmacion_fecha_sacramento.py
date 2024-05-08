# Generated by Django 5.0.4 on 2024-05-08 07:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confirmacion', '0002_alter_confirmacion_fecha_sacramento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmacion',
            name='fecha_sacramento',
            field=models.DateField(default=django.utils.timezone.now, help_text='Fecha cuando se ejerció el sacramento.'),
        ),
    ]
