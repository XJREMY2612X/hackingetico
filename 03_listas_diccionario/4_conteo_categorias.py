# 4. Contar por categoría[cite: 11]
vulnerabilidades = [
    {"title": "SQLi", "owasp_category": "A1"},
    {"title": "XSS", "owasp_category": "A3"},
    {"title": "Broken Auth", "owasp_category": "A1"}
]

conteo = {}
for vuln in vulnerabilidades:
    cat = vuln.get("owasp_category")
    conteo[cat] = conteo.get(cat, 0) + 1

print("Conteo de categorías:", conteo)
