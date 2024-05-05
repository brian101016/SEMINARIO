# Generated by Django 5.0.4 on 2024-05-04 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=24)),
                ('can_write', models.BooleanField(default=False)),
                ('super_admin', models.BooleanField(default=False)),
            ],
        ),
    ]