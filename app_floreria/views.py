from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedido, Cliente, Producto

# ==========================================
# PÁGINA DE INICIO
# ==========================================
def inicio(request):
    return render(request, 'inicio.html')

# ==========================================
# AGREGAR PEDIDO (sin pedir ID)
# ==========================================
def agregar_pedido(request):
    if request.method == 'POST':
        # Leer los datos del formulario
        nombre_cliente = request.POST.get('nombre_cliente')
        nombre_producto = request.POST.get('nombre_producto')

        # Si el cliente no existe, se crea automáticamente
        cliente, _ = Cliente.objects.get_or_create(
            nombre=nombre_cliente,
            defaults={
                'apellido': '',
                'telefono': '',
                'email': '',
                'direccion': '',
                'ciudad': '',
                'codigo_postal': ''
            }
        )

        # Si el producto no existe, también se crea automáticamente
        producto, _ = Producto.objects.get_or_create(
            nombre=nombre_producto,
            defaults={
                'descripcion': '',
                'precio': 0,
                'stock': 1,
                'categoria': '',
                'proveedor': '',
                'fecha_agregado': '2025-01-01'
            }
        )

        # Crear el pedido
        Pedido.objects.create(
            cliente=cliente,
            producto=producto,
            fecha_pedido=request.POST.get('fecha_pedido'),
            fecha_entrega=request.POST.get('fecha_entrega'),
            total=request.POST.get('total'),
            estado=request.POST.get('estado'),
            metodo_pago=request.POST.get('metodo_pago'),
            direccion_envio=request.POST.get('direccion_envio')
        )

        return redirect('ver_pedido')

    return render(request, 'pedido/agregar_pedido.html')

# ==========================================
# VER PEDIDOS
# ==========================================
def ver_pedido(request):
    pedidos = Pedido.objects.select_related('cliente', 'producto').all()
    return render(request, 'pedido/ver_pedido.html', {'pedidos': pedidos})

# ==========================================
# ACTUALIZAR PEDIDO
# ==========================================
def actualizar_pedido(request, id_pedido):
    pedido = get_object_or_404(Pedido, id_pedido=id_pedido)

    if request.method == 'POST':
        pedido.estado = request.POST.get('estado')
        pedido.metodo_pago = request.POST.get('metodo_pago')
        pedido.fecha_entrega = request.POST.get('fecha_entrega')
        pedido.total = request.POST.get('total')
        pedido.direccion_envio = request.POST.get('direccion_envio')
        pedido.save()
        return redirect('ver_pedido')

    return render(request, 'pedido/actualizar_pedido.html', {'pedido': pedido})

# ==========================================
# BORRAR PEDIDO
# ==========================================
def borrar_pedido(request, id_pedido):
    pedido = get_object_or_404(Pedido, id_pedido=id_pedido)
    pedido.delete()
    return redirect('ver_pedido')
