# Generated by Django 3.2.15 on 2023-08-17 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ficha.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ficha', '0027_auto_20230817_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='observacion',
            name='usuario_revisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='observaciones_revisor', to=settings.AUTH_USER_MODEL),
        ),
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
