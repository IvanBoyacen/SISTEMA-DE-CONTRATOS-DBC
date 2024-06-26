# Generated by Django 4.1.2 on 2024-04-23 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpresaSST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_documento', models.CharField(max_length=255, verbose_name='Nombre Documento')),
                ('tipo_documento', models.CharField(choices=[('Capacitaciones', 'Capacitaciones'), ('Comité COPASST', 'Comité COPASST'), ('Comité Convivencia', 'Comité Convivencia'), ('Otros', 'Otros')], max_length=50, verbose_name='Tipo de Documento')),
                ('archivo', models.FileField(null=True, upload_to='archivos/', verbose_name='Archivo')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de Creación')),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
            ],
        ),
    ]
