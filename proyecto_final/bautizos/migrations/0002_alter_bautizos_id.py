from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bautizos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bautizos',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]