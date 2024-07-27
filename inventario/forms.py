# forms.py
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from api.models import *

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['catalogo','cantidad','estacion','almacen','transporte']

    def __init__(self, *args, **kwargs):
        super(StockForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar Proveedor'))
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'