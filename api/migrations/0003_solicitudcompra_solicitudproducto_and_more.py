# Generated by Django 5.0.2 on 2024-07-27 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_descripccion_catalogue_descripcion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20, unique=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('entrega', models.DateField()),
                ('pago', models.CharField(max_length=100)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(max_length=50)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.catalogue')),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.solicitudcompra')),
            ],
        ),
        migrations.AddField(
            model_name='solicitudcompra',
            name='productos',
            field=models.ManyToManyField(through='api.SolicitudProducto', to='api.catalogue'),
        ),
    ]
