# Generated by Django 5.0.4 on 2024-05-08 07:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Confirmacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_sacramento', models.DateField(default=datetime.date(2024, 5, 8), help_text='Fecha cuando se ejerció el sacramento.')),
                ('presbitero', models.CharField(help_text='Nombre completo del presbítero a cargo.', max_length=100)),
                ('libro', models.PositiveSmallIntegerField(default=1, help_text='Representa el número del libro según el sacramento.')),
                ('pagina', models.PositiveSmallIntegerField(default=1, help_text='Representa el número de página según el libro.')),
                ('partida', models.PositiveSmallIntegerField(default=1, help_text='Representa el número de partida según la página.')),
                ('notas', models.CharField(help_text='Cualquier consideración o notas adicionales.', max_length=1000)),
                ('nombre', models.CharField(help_text='Nombre completo de quien recibe el sacramento.', max_length=100)),
                ('sexo', models.BooleanField(help_text="Sexo según: 'False' para hombre, 'True' para mujer.")),
                ('padre', models.CharField(help_text='Nombre completo del padre.', max_length=100)),
                ('madre', models.CharField(help_text='Nombre completo de la madre.', max_length=100)),
                ('padrino_madrina', models.CharField(help_text='Nombre completo del padrino o madrina.', max_length=100)),
                ('ciudad_bautizo', models.CharField(default='Hermosillo, Sonora', help_text='Ciudad donde se recibió el bautismo.', max_length=100)),
                ('parroquia_bautizo', models.CharField(help_text='Parroquia donde se recibió el bautismo.', max_length=100)),
                ('fecha_bautizo', models.DateField(help_text='Fecha de cuando se recibió el bautismo.')),
            ],
            options={
                'ordering': ['-fecha_sacramento', 'nombre'],
            },
        ),
    ]
