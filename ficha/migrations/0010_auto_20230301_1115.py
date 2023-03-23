# Generated by Django 3.2.15 on 2023-03-01 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0009_caracteristicasmorfologicas_descripcion_del_inmubebles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteristicasmorfologicas',
            name='materialidad_revestimientos',
            field=models.CharField(blank=True, choices=[('ENLUCIDO/ESTUCO', 'Enlucido/estuco'), ('MADERA', 'Madera'), ('PLACHA TOLENADA', 'Placha tolenada'), ('HORMIGON ', 'Hormigo a la vista'), ('OTROS', 'Otros')], default='ENLUCIDO/ESTUCO', max_length=255),
        ),
        migrations.AlterField(
            model_name='relaciondelinmuebleconelterreno',
            name='Otros_elementos_patrimonial',
            field=models.TextField(blank=True, choices=[('PLACA EN FACHADA', 'Placa en fachada'), ('ESCULTURA', 'Escultura'), ('MONUMENTOS PUBLICOS', 'Monumentos publicos'), ('RELACION VISUAL', 'Relacion visual'), ('OTROS', 'Otros')], default='PLACA EN FACHADA'),
        ),
    ]