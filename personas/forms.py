from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column, Submit
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Crear', style='background-color: #003594;'))
        self.helper.layout = Layout(
            Fieldset(
                'DATOS DE LA PERSONA',
                Row(
                    Column('nombre_persona', css_class='form-group col-md-4 mb-3'),
                    Column('tipo_documento_persona', css_class='form-group col-md-4 mb-3'),
                    Column('numero_documento_persona', css_class='form-group col-md-4 mb-3'),
                ),
                Row(
                    Column('correo_persona', css_class='form-group col-md-4 mb-3'),
                    Column('celular_persona', css_class='form-group col-md-4 mb-3'),
                    Column('direccion_residencia_persona', css_class='form-group col-md-4 mb-3'),
                ),
                css_class='seccion-container'
            ),
        )
        
class PersonaEditForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PersonaEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar Cambios', style='background-color: #003594;'))
        self.helper.layout = Layout(
            Fieldset(
                'DATOS DE LA PERSONA',
                Row(
                    Column('nombre_persona', css_class='form-group col-md-4 mb-3'),
                    Column('tipo_documento_persona', css_class='form-group col-md-4 mb-3'),
                    Column('numero_documento_persona', css_class='form-group col-md-4 mb-3'),
                ),
                Row(
                    Column('correo_persona', css_class='form-group col-md-4 mb-3'),
                    Column('celular_persona', css_class='form-group col-md-4 mb-3'),
                    Column('direccion_residencia_persona', css_class='form-group col-md-4 mb-3'),
                ),
                css_class='seccion-container'
            ),
        )
