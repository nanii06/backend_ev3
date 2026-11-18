from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils import timezone


CATEGORIAS = [
    ('Fútbol', 'Fútbol'),
    ('Running', 'Running'),
    ('Tenis', 'Tenis'),
    ('Básquetbol', 'Básquetbol'),
    ('Natación', 'Natación'),
]

def validar_fecha_ingreso(fecha):
    if fecha > timezone.localdate():
        raise ValidationError('La fecha de ingreso no puede ser futura.')

class Producto(models.Model):
    nombre = models.CharField(max_length=150, validators=[MinLengthValidator(4, message='El nombre debe tener al menos 4 caracteres.')])
    descripcion = models.TextField(validators=[MinLengthValidator(10, message='La descripción debe tener al menos 10 caracteres.')])
    stock = models.PositiveIntegerField(validators=[MinValueValidator(1, message='El stock debe ser al menos 1.')])
    precio_unitario = models.PositiveIntegerField(validators=[MinValueValidator(1, message='El precio debe ser al menos 1.')])
    fecha_ingreso = models.DateField(validators=[validar_fecha_ingreso])
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        nombre = ' '.join(self.nombre.split())
        self.nombre = nombre[:1].upper() + nombre[1:]
        descripcion = self.descripcion.strip()
        self.descripcion = descripcion[:1].upper() + descripcion[1:]
        super().save(*args, **kwargs)


