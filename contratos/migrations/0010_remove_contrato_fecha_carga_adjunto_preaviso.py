# Generated by Django 4.1.2 on 2024-05-30 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0009_contrato_consecutivo_contrato_dias_restantes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrato',
            name='fecha_carga_adjunto_preaviso',
        ),
    ]