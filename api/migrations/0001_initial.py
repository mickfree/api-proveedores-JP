<<<<<<< HEAD
# Generated by Django 5.0.2 on 2024-07-15 17:46

import django.db.models.deletion
=======
# Generated by Django 5.0.2 on 2024-07-11 16:01

>>>>>>> 4e8dbca1ea3a1fcb5201a3424a90bf5c3445a249
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('nombre_empresa', models.CharField(max_length=100)),
                ('ruc', models.CharField(max_length=13, unique=True)),
                ('direccion', models.CharField(max_length=255)),
                ('nombre_contacto', models.CharField(max_length=100)),
=======
                ('ruc', models.CharField(max_length=13, unique=True)),
                ('direccion', models.CharField(max_length=255)),
                ('nombre_contacto', models.CharField(max_length=100)),
                ('items', models.TextField()),
>>>>>>> 4e8dbca1ea3a1fcb5201a3424a90bf5c3445a249
                ('telefonos', models.CharField(max_length=100)),
                ('observaciones', models.TextField(blank=True, null=True)),
            ],
        ),
<<<<<<< HEAD
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('precio', models.CharField(max_length=50)),
                ('descripccion', models.CharField(max_length=250)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('estacion', models.CharField(max_length=100)),
                ('almacen', models.CharField(max_length=100)),
                ('transporte', models.CharField(max_length=100)),
                ('catalogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.catalogue')),
            ],
        ),
=======
>>>>>>> 4e8dbca1ea3a1fcb5201a3424a90bf5c3445a249
    ]
