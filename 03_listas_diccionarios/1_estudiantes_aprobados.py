# 1. Estudiantes que aprobaron[cite: 11]
estudiantes = [
    {"name": "Ana", "grade": 8},
    {"name": "Luis", "grade": 5},
    {"name": "Eva", "grade": 9}
]

aprobados = [estudiante["name"] for estudiante in estudiantes if estudiante.get("grade", 0) >= 7]
print("Aprobados:", aprobados)
