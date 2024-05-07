# Generated by Django 5.0.4 on 2024-05-05 05:12

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
                ('nombre', models.CharField(help_text='Nombre completo de quien recibe el sacramento.', max_length=200)),
                ('sexo', models.BooleanField(default=False, help_text="Sexo según: 'False' para hombre, 'True' para mujer.")),
                ('padre', models.CharField(help_text='Nombre completo del padre.', max_length=200)),
                ('madre', models.CharField(help_text=' Nombre completo de la madre.', max_length=200)),
                ('padrino_madrina', models.CharField(help_text='Nombre completo del padrino o madrina.', max_length=200)),
                ('parroquia_bautizo', models.CharField(help_text='Parroquia donde se recibió el bautismo.', max_length=100)),
                ('ciudad_bautizo', models.CharField(help_text='Ciudad donde se recibió el bautismo.', max_length=50)),
                ('fecha_bautizo', models.DateField(auto_now=True, help_text='Fecha de cuando se recibió el bautismo.')),
            ],
        ),
    ]
