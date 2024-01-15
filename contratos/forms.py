from django import forms
from .models import Contratos

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contratos
        fields = '__all__'
