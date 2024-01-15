from django.shortcuts import render, redirect, get_object_or_404
from .models import Contratos
from .forms import ContratoForm


def contratos(request):
    contratos_list = Contratos.objects.all()
    return render(request, 'contratos/contratos.html', {'contratos': contratos_list})

def crear_contrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST, request.FILES) 
        if form.is_valid():
            contrato = form.save()
            return redirect('detalles_contrato', contrato_id=contrato.id)
        else:
            print("Formulario no válido. Errores:", form.errors)
    else:
        form = ContratoForm()

    return render(request, 'contratos/crear_contrato.html', {'form': form})



def detalles_contrato(request, contrato_id):
    contrato = get_object_or_404(Contratos, id=contrato_id)
    return render(request, 'contratos/contratoDetalles.html', {'contrato': contrato})

def editar_contrato(request, contrato_id):
    contrato = get_object_or_404(Contratos, id=contrato_id)
    if request.method == 'POST':
        form = ContratoForm(request.POST, instance=contrato)
        if form.is_valid():
            form.save()
            return redirect('detalles_contrato', contrato_id=contrato.id)
    else:
        form = ContratoForm(instance=contrato)

    return render(request, 'contratos/editar_contrato.html', {'form': form, 'contrato': contrato})
