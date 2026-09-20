carrito = [
    {'articulo': 'laptop', 'precio': 800},
    {'articulo': 'raton', 'precio': 25},
    {'articulo': 'teclado', 'precio': 45}
]
total = 0
for articulo in carrito:
    total += articulo['precio']
print(f"Total acumulado: {total}")
