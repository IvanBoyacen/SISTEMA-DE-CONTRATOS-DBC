from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

class Contratos(models.Model):
    # DATOS DE LA EMPRESA
    razón_social = models.CharField(max_length=255, default='DIGITAL BRIDGE COMMUNICATIONS WORLWIDE S.A.S')
    nit_empresa = models.CharField(max_length=20, default='901481430')
    nombre_representante = models.CharField(max_length=255, default='Jonathan Cifuentes')
    cargo_representante = models.CharField(max_length=255, default='Gerente')
    tipo_documento_empleador = models.CharField(max_length=255, choices=[("CC", "Cédula de Ciudadanía"), ("CE", "Cédula de Extranjería"), ("P", "Pasaporte")], default='CC')
    numero_documento_empleador = models.CharField(max_length=20, default='000')
    lugar_expedicion_cc_empleador = models.CharField(max_length=255, default='NA')
    celular_empleador = models.CharField(max_length=20, default='+1 (336) 899-7553')
    correo_electronico_empleador = models.EmailField(max_length=255, default='jcifuentes@dbcw.com.co')
    direccion_empresa = models.CharField(max_length=255, default='Jenesano-Boyacá')

    # DATOS DEL EMPLEADO
    nombre_empleado = models.CharField(max_length=255)
    tipo_documento_empleado = models.CharField(max_length=255, choices=[("CC", "Cédula de Ciudadanía"), ("CE", "Cédula de Extranjería"), ("P", "Pasaporte")])
    numero_documento_empleado = models.CharField(max_length=20, default='No especificado')  
    correo_empleado = models.EmailField()
    celular_empleado = models.CharField(max_length=20)
    direccion_residencia_empleado = models.CharField(max_length=255)

    # DATOS DEL CONTRATO
    tipo_contrato = models.CharField(max_length=255)
    cargo_contrato = models.CharField(max_length=255)
    salario = models.DecimalField(max_digits=10, decimal_places=2, help_text="Ingrese el salario en el formato XX.XX")
    duracion_contrato = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_terminacion = models.DateField()
    fecha_pre_aviso = models.DateField()

    # ADJUNTOS CONTRATOS
    adjunto_contrato_1 = models.FileField(upload_to='adjuntos_contratos/')
    fecha_carga_adjunto_1 = models.DateField()

    # ADJUNTOS PRE AVISO
    adjunto_preaviso_4 = models.FileField(upload_to='adjuntos_preaviso/')
    fecha_carga_adjunto_4 = models.DateField()

    def __str__(self):
        return self.tipo_contrato

@receiver(pre_save, sender=Contratos)
def actualizar_fecha_carga_adjunto(sender, instance, **kwargs):
    # Actualizar la fecha de carga del adjunto antes de guardar
    instance.fecha_carga_adjunto_1 = timezone.now().date()
    instance.fecha_carga_adjunto_4 = timezone.now().date()
