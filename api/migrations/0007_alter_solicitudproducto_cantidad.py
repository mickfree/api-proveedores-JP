# Generated by Django 5.0.2 on 2024-07-27 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_solicitudcompra_productos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudproducto',
            name='cantidad',
            field=models.PositiveIntegerField(),
        ),
    ]
