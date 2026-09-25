# 1. Conversor de temperatura[cite: 9]
def celsius_to_fahrenheit(c):
    try:
        return (float(c) * 9/5) + 32
    except (ValueError, TypeError):
        return "Error: Entrada no numérica"

def fahrenheit_to_celsius(f):
    try:
        return (float(f) - 32) * 5/9
    except (ValueError, TypeError):
        return "Error: Entrada no numérica"
