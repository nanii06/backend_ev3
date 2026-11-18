from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductoForm
from .models import Producto


@login_required
@permission_required('deportesApp.view_producto', raise_exception=True)
def listar_productos(request):
    busqueda = request.GET.get('q', '').strip()
    productos = Producto.objects.order_by('nombre')
    if busqueda:
        productos = productos.filter(nombre__icontains=busqueda)
    contexto = {'productos': productos, 'busqueda': busqueda}
    return render(request, 'deportesApp/listar_productos.html', contexto)


@login_required
@permission_required('deportesApp.add_producto', raise_exception=True)
def agregar_producto(request):
    formulario = ProductoForm(request.POST or None)
    if request.method == 'POST' and formulario.is_valid():
        formulario.save()
        messages.success(request, 'Producto agregado correctamente.')
        return redirect('listar_productos')
    return render(request, 'deportesApp/formulario_productos.html',
                  {'formulario': formulario, 'titulo': 'Agregar producto'})


@login_required
@permission_required('deportesApp.change_producto', raise_exception=True)
def modificar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    formulario = ProductoForm(request.POST or None, instance=producto)
    if request.method == 'POST' and formulario.is_valid():
        formulario.save()
        messages.success(request, 'Producto modificado correctamente.')
        return redirect('listar_productos')
    return render(request, 'deportesApp/formulario_productos.html',
                  {'formulario': formulario, 'titulo': 'Modificar producto'})


@login_required
@permission_required('deportesApp.delete_producto', raise_exception=True)
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado correctamente.')
        return redirect('listar_productos')
    return render(request, 'deportesApp/confirmar_eliminar.html', {'producto': producto})
