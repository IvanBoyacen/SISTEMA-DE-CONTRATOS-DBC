from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

class Contratos(models.Model):
    # DATOS DEL EMPLEADOR
    nombre_empresa = models.CharField(max_length=255)
    representante = models.CharField(max_length=255)
    cargo_empleador = models.CharField(max_length=255)
    cc_empleador = models.PositiveIntegerField()
    lugar_expedicion_cc_empleador = models.CharField(max_length=255)
    celular_empleador = models.CharField(max_length=20)
    correo_electronico_empleador = models.EmailField()
    direccion_residencia_empleador = models.CharField(max_length=255)

    # DATOS DEL EMPLEADO
    nombre_empleado = models.CharField(max_length=255)
    cc_empleado = models.PositiveIntegerField()
    correo_empleado = models.EmailField()
    celular_empleado = models.CharField(max_length=20)
    direccion_residencia_empleado = models.CharField(max_length=255)

    # DATOS DEL CONTRATO
    cargo_contrato = models.CharField(max_length=255)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_contrato = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_terminacion = models.DateField()
    tipo_contrato = models.CharField(max_length=255)

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
