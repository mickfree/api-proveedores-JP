# Generated by Django 5.0.2 on 2024-07-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalogue',
            old_name='descripccion',
            new_name='descripcion',
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
