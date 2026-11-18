from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    fecha_ingreso = forms.DateField(
        label='Fecha de ingreso',
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(
            format='%d-%m-%Y',
            attrs={'class': 'form-control', 'placeholder': 'dd-mm-aaaa'},
        ),
    )

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'stock', 'precio_unitario', 'fecha_ingreso', 'categoria']
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'stock': 'Stock',
            'precio_unitario': 'Precio unitario',
            'categoria': 'Categoría',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()
        if not nombre:
            raise forms.ValidationError('El nombre no puede estar vacío.')
        return nombre

