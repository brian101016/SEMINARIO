from django.db import migrations, models


class Migration(migrations.Migration):


    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bautizos',
            fields = [
                
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('sexo', models.BooleanField(initial = True)),
                ('fecha_nacimiento', models.DateField()),
                ('ciudad_nacimiento', models.CharField(max_length=60)),
                ('folio_acta_nacimiento', models.CharField(max_length=60)),
                ('padre', models.CharField(max_length=60)),
                ('madre', models.CharField(max_length=60)),
                ('abuelos_paternos', models.CharField(max_length=60)),
                ('abuelos_maternos', models.CharField(max_length=60)),
                ('padrino', models.CharField(max_length=60)),
                ('madrina', models.CharField(max_length=60)),
                ('fecha_sacramento', models.DateField()),
                ('presbitero', models.CharField(max_length=60)),
                ('libro', models.IntegerField()),
                ('pagina', models.IntegerField()),
                ('partida', models.IntegerField()),
                ('notas', models.CharField(max_length=60)),

            ],
        ),
    ]
  