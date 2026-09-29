estudiantes = [
    {'nombre': 'Ana', 'presente': True},
    {'nombre': 'Luis', 'presente': False},
    {'nombre': 'Carlos', 'presente': False}
]
for estudiante in estudiantes:
    if not estudiante['presente']:
        print(estudiante['nombre'])
