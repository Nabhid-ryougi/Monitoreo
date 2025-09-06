from django import forms
from .models import Dispositivo


class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        field = '__all__'

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre_dispositivos')


        if len(nombre) < 3 :
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres')
        
        return nombre