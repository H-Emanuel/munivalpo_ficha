# Generated by Django 3.2.15 on 2023-08-17 20:35

from django.db import migrations, models
import ficha.models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografiacontexto',
            name='registro_fotografico_1',
            field=models.ImageField(blank=True, default='', upload_to=ficha.models.content_file_name_contexto_1),
        ),
        migrations.AlterField(
            model_name='fotografiacontexto',
            name='registro_fotografico_2',
            field=models.ImageField(blank=True, default='', upload_to=ficha.models.content_file_name_contexto_2),
        ),
    ]
