from django.urls import path
from contratos.views import contrato, detalles_contrato, editar_contrato, crear_contrato

urlpatterns = [
    path('', contrato, name="contratos"),
    path('contratos/detalles/<int:contrato_id>/', detalles_contrato, name="detalles_contrato"),
    path('contratos/editar/<int:contrato_id>/', editar_contrato, name="editar_contrato"),
    path('contratos/crear/', crear_contrato, name="crear_contrato"),
]