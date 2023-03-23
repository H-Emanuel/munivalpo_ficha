# Generated by Django 3.2.15 on 2023-02-28 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0006_alter_informaciontecnica_piso_original_subterraneo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informaciontecnica',
            name='piso_actual_pisos_superiores',
            field=models.CharField(blank=True, choices=[('VIVIENDA', 'Vivienda'), ('COMERCIO', 'Comercio'), ('SERVICIO', 'Servicio'), ('EDUCACION', 'Educacion'), ('SALUD', 'Salud'), ('DEPORTE', 'Deporte'), ('RECREACION', 'Recreacion'), ('CULTURA', 'Cultura'), ('CULTO', 'Culto'), ('INDUSTRIA', 'Industria'), ('BODEGA', 'Bodega')], default='VIVIENDA', max_length=255),
        ),
        migrations.AlterField(
            model_name='informaciontecnica',
            name='piso_actual_primer_piso',
            field=models.CharField(blank=True, choices=[('VIVIENDA', 'Vivienda'), ('COMERCIO', 'Comercio'), ('SERVICIO', 'Servicio'), ('EDUCACION', 'Educacion'), ('SALUD', 'Salud'), ('DEPORTE', 'Deporte'), ('RECREACION', 'Recreacion'), ('CULTURA', 'Cultura'), ('CULTO', 'Culto'), ('INDUSTRIA', 'Industria'), ('BODEGA', 'Bodega')], default='VIVIENDA', max_length=255),
        ),
        migrations.AlterField(
            model_name='informaciontecnica',
            name='piso_actual_subterraneo',
            field=models.CharField(blank=True, choices=[('VIVIENDA', 'Vivienda'), ('COMERCIO', 'Comercio'), ('SERVICIO', 'Servicio'), ('EDUCACION', 'Educacion'), ('SALUD', 'Salud'), ('DEPORTE', 'Deporte'), ('RECREACION', 'Recreacion'), ('CULTURA', 'Cultura'), ('CULTO', 'Culto'), ('INDUSTRIA', 'Industria'), ('BODEGA', 'Bodega')], default='VIVIENDA', max_length=255),
        ),
        migrations.AlterField(
            model_name='informaciontecnica',
            name='piso_original_pisos_superiores',
            field=models.CharField(blank=True, choices=[('VIVIENDA', 'Vivienda'), ('COMERCIO', 'Comercio'), ('SERVICIO', 'Servicio'), ('EDUCACION', 'Educacion'), ('SALUD', 'Salud'), ('DEPORTE', 'Deporte'), ('RECREACION', 'Recreacion'), ('CULTURA', 'Cultura'), ('CULTO', 'Culto'), ('INDUSTRIA', 'Industria'), ('BODEGA', 'Bodega')], default='VIVIENDA', max_length=255),
        ),
        migrations.AlterField(
            model_name='informaciontecnica',
            name='piso_original_primer_piso',
            field=models.CharField(blank=True, choices=[('VIVIENDA', 'Vivienda'), ('COMERCIO', 'Comercio'), ('SERVICIO', 'Servicio'), ('EDUCACION', 'Educacion'), ('SALUD', 'Salud'), ('DEPORTE', 'Deporte'), ('RECREACION', 'Recreacion'), ('CULTURA', 'Cultura'), ('CULTO', 'Culto'), ('INDUSTRIA', 'Industria'), ('BODEGA', 'Bodega')], default='VIVIENDA', max_length=255),
        ),
    ]