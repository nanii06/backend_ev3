
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductoForm
from .models import Producto


def es_administrador(usuario):
    return usuario.is_superuser or usuario.groups.filter(name='Administrador').exists()


@login_required
def listar_productos(request):
    busqueda = request.GET.get('q', '').strip()
    productos = Producto.objects.select_related('categoria').order_by('nombre')
    if busqueda:
        productos = productos.filter(nombre__icontains=busqueda)
    contexto = {
        'productos': productos,
        'busqueda': busqueda,
        'es_administrador': es_administrador(request.user),
    }
    return render(request, 'deportesApp/listar_productos.html', contexto)


@user_passes_test(es_administrador, login_url='login')
def agregar_producto(request):
    formulario = ProductoForm(request.POST or None)
    if request.method == 'POST' and formulario.is_valid():
        formulario.save()
        messages.success(request, 'Producto agregado correctamente.')
        return redirect('listar_productos')
    return render(request, 'deportesApp/formulario_producto.html',
                  {'formulario': formulario, 'titulo': 'Agregar producto'})


@user_passes_test(es_administrador, login_url='login')
def modificar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    formulario = ProductoForm(request.POST or None, instance=producto)
    if request.method == 'POST' and formulario.is_valid():
        formulario.save()
        messages.success(request, 'Producto modificado correctamente.')
        return redirect('listar_productos')
    return render(request, 'deportesApp/formulario_producto.html',
                  {'formulario': formulario, 'titulo': 'Modificar producto'})


@user_passes_test(es_administrador, login_url='login')
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado correctamente.')
        return redirect('listar_productos')
    return render(request, 'deportesApp/confirmar_eliminar.html', {'producto': producto})