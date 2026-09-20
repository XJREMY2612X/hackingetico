usuarios = [
    {'nombre': 'Usuario1', 'rol': 'admin'},
    {'nombre': 'Usuario2', 'rol': 'editor'},
    {'nombre': 'Usuario3', 'rol': 'editor'},
    {'nombre': 'Usuario4', 'rol': 'espectador'}
]
roles_unicos = []
for usuario in usuarios:
    if usuario['rol'] not in roles_unicos:
        roles_unicos.append(usuario['rol'])
print(roles_unicos)
