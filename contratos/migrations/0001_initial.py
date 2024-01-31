# Generated by Django 4.1.2 on 2024-01-29 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contratos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razón_social', models.CharField(max_length=255)),
                ('nit_empresa', models.CharField(max_length=20)),
                ('nombre_representante', models.CharField(max_length=255)),
                ('cargo_representante', models.CharField(max_length=255)),
                ('tipo_documento_empleador', models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('P', 'Pasaporte')], max_length=255)),
                ('numero_documento_empleador', models.CharField(max_length=20)),
                ('lugar_expedicion_cc_empleador', models.CharField(max_length=255)),
                ('celular_empleador', models.CharField(max_length=20)),
                ('correo_electronico_empleador', models.EmailField(max_length=254)),
                ('direccion_residencia_empleador', models.CharField(max_length=255)),
                ('nombre_empleado', models.CharField(max_length=255)),
                ('tipo_documento_empleado', models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('P', 'Pasaporte')], max_length=255)),
                ('numero_documento_empleado', models.CharField(default='No especificado', max_length=20)),
                ('correo_empleado', models.EmailField(max_length=254)),
                ('celular_empleado', models.CharField(max_length=20)),
                ('direccion_residencia_empleado', models.CharField(max_length=255)),
                ('tipo_contrato', models.CharField(max_length=255)),
                ('cargo_contrato', models.CharField(max_length=255)),
                ('salario', models.DecimalField(decimal_places=2, help_text='Ingrese el salario en el formato XX.XX', max_digits=10)),
                ('duracion_contrato', models.CharField(max_length=255)),
                ('fecha_inicio', models.DateField()),
                ('fecha_terminacion', models.DateField()),
                ('fecha_pre_aviso', models.DateField()),
                ('adjunto_contrato_1', models.FileField(upload_to='adjuntos_contratos/')),
                ('fecha_carga_adjunto_1', models.DateField()),
                ('adjunto_preaviso_4', models.FileField(upload_to='adjuntos_preaviso/')),
                ('fecha_carga_adjunto_4', models.DateField()),
            ],
        ),
    ]
