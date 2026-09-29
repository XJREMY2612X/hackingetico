# 5. Excepción personalizada[cite: 9]
class InvalidGradeError(Exception):
    pass

def procesar_calificacion(nota):
    if not (0 <= nota <= 10):
        raise InvalidGradeError(f"La nota {nota} está fuera del rango 0-10")
    return f"Nota {nota} procesada con éxito"
