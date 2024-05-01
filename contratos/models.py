from django.db import models
from personas.models import Persona
from cargos.models import Cargo
from django.utils import timezone
import locale


class Contrato(models.Model):
    razón_social = models.CharField(max_length=255, default='DIGITAL BRIDGE COMMUNICATIONS')
    nit_empresa = models.CharField(max_length=20, default='9014814305')
    nombre_representante_legal = models.CharField(max_length=255, default='Jonathan Cifuentes Cadena')
    cargo_representante_legal = models.CharField(max_length=255, default='Gerente')
    tipo_doc_representante_legal = models.CharField(max_length=255, choices=[("CC", "Cédula de Ciudadanía"), ("CE", "Cédula de Extranjería"), ("P", "Pasaporte")], default='CC')
    numero_doc_representante_legal = models.CharField(max_length=20, default='1016019519')
    lugar_expedicion_doc_representante_legal = models.CharField(max_length=255, default='Bogotá')
    celular_representante_legal = models.CharField(max_length=20, default='+1 (336) 899-7553')
    correo_representante_legal = models.EmailField(max_length=255, default='jcifuentes@dbcw.com.co')
    ubicacion = models.CharField(max_length=255, default='Jenesano-Boyacá')
    direccion_notificacion_judicial= models.CharField(max_length=255, default='Cl. #8-42')

    empleado = models.ForeignKey(Persona, on_delete=models.CASCADE)

    TIPO_CONTRATO_CHOICES = [
        ('Contrato de Trabajo a Tiempo Completo - Término Fijo', 'Contrato de Trabajo a Tiempo Completo - Término Fijo'),
        ('Contrato de Trabajo a Tiempo Parcial - Término Fijo', 'Contrato de Trabajo a Tiempo Parcial - Término Fijo'),
        ('Contrato de Aprendizaje', 'Contrato de Aprendizaje'),
    ]
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Terminado', 'Terminado'),
    ]
    cargo_contrato = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    tipo_contrato = models.CharField(max_length=255, choices=TIPO_CONTRATO_CHOICES)
    salario = models.DecimalField(max_digits=10, decimal_places=0) 

    def formato_salario(self):
        
        locale.setlocale(locale.LC_ALL, '')

        salario_formateado = locale.currency(self.salario, grouping=True)

        return salario_formateado
    duracion_contrato = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_terminacion = models.DateField()
    fecha_pre_aviso = models.DateField()
    estado = models.CharField(max_length=100, choices=ESTADO_CHOICES, default='Activo')
    fecha_creacion_contrato = models.DateField(auto_now_add=True)  
    adjunto_contrato = models.FileField(upload_to='adjuntos_contratos/')
    fecha_carga_adjunto_contrato = models.DateField(auto_now_add=True)
    adjunto_preaviso = models.FileField(upload_to='adjuntos_preaviso/')
    fecha_carga_adjunto_preaviso = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_contrato} - Salario: ${self.salario:,.0f}"
