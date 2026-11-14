from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    stock = models.PositiveIntegerField()
    precio_unitario = models.PositiveIntegerField()
    fecha_ingreso = models.DateField()
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='productos',
    )

    def __str__(self):
        return self.nombre