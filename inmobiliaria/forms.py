
from django import forms
from .models import (
    Propiedad, Cliente_Inmobiliaria, Propietario, Agente_Inmobiliario, 
    Visita_Propiedad, Contrato_Venta, Contrato_Alquiler
)

class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'direccion_propietario': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = '__all__'
        widgets = {
            'propietario': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_propiedad': forms.TextInput(attrs={'class': 'form-control'}),
            'num_habitaciones': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_banos': forms.NumberInput(attrs={'class': 'form-control'}),
            'superficie_m2': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_venta': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_alquiler': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado_propiedad': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class Cliente_InmobiliariaForm(forms.ModelForm):
    class Meta:
        model = Cliente_Inmobiliaria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'preferencias_propiedad': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'presupuesto_maximo': forms.NumberInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
        }

class Agente_InmobiliarioForm(forms.ModelForm):
    class Meta:
        model = Agente_Inmobiliario
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'licencia_agente': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_contratacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'salario': forms.NumberInput(attrs={'class': 'form-control'}),
            'comision_porcentaje': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class Visita_PropiedadForm(forms.ModelForm):
    class Meta:
        model = Visita_Propiedad
        fields = '__all__'
        widgets = {
            'propiedad': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'agente': forms.Select(attrs={'class': 'form-control'}),
            'fecha_visita': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora_visita': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'comentarios_cliente': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'calificacion_propiedad': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class Contrato_VentaForm(forms.ModelForm):
    class Meta:
        model = Contrato_Venta
        fields = '__all__'
        widgets = {
            'propiedad': forms.Select(attrs={'class': 'form-control'}),
            'propietario': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'agente': forms.Select(attrs={'class': 'form-control'}),
            'fecha_contrato': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'precio_final': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_cierre': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado_contrato': forms.TextInput(attrs={'class': 'form-control'}),
            'comision_agente': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class Contrato_AlquilerForm(forms.ModelForm):
    class Meta:
        model = Contrato_Alquiler
        fields = '__all__'
        widgets = {
            'propiedad': forms.Select(attrs={'class': 'form-control'}),
            'propietario': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'agente': forms.Select(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'monto_alquiler_mensual': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado_contrato': forms.TextInput(attrs={'class': 'form-control'}),
            'deposito_garantia': forms.NumberInput(attrs={'class': 'form-control'}),
        }
