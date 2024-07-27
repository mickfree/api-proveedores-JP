from django import forms
from api.models import SolicitudCompra, Catalogue, Proveedor

# class SolicitudCompraForm(forms.ModelForm):
    
#     class Meta:
#         model = SolicitudCompra
#         fields = ['numero','proveedor', 'entrega', 'pago', 'estado']
#         widgets = {
#             'entrega': forms.DateInput(attrs={'type': 'date'}),
#             'pago': forms.DateInput(attrs={'type': 'date'}),
#         }

    # productos = forms.ModelMultipleChoiceField(
    #     queryset=Catalogue.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    # )

#     def __init__(self, *args, **kwargs):
#         super(SolicitudCompraForm, self).__init__(*args, **kwargs)
#         self.fields['proveedor'].queryset = Proveedor.objects.all()
        
class SolicitudCompraForm(forms.ModelForm):
    class Meta:
        model = SolicitudCompra
        fields = ['numero','proveedor', 'entrega', 'pago', 'estado']
        widgets = {
            'entrega': forms.DateInput(attrs={'type': 'date'}),
            'pago': forms.DateInput(attrs={'type': 'date'}),
        }
            
    productos = forms.ModelMultipleChoiceField(
        queryset=Catalogue.objects.all(),
        widget=forms.CheckboxSelectMultiple,)

    def __init__(self, *args, **kwargs):
        super(SolicitudCompraForm, self).__init__(*args, **kwargs)
        self.fields['proveedor'].queryset = Proveedor.objects.all()
        
        
class AddProductosForm(forms.Form):
    productos = forms.ModelMultipleChoiceField(
        queryset=Catalogue.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False  # Hacer que el campo sea opcional
    )