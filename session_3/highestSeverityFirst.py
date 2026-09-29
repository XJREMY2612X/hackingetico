# 1. Definición de la función solicitada en el ejercicio 5
def sort_vulnerabilities(vulnerabilities):
    # sorted() toma la lista, la clave de ordenamiento (lambda) y reverse=True para orden descendente
    return sorted(vulnerabilities, key=lambda vuln: vuln['severity'], reverse=True)


# 2. Bloque principal para probar el funcionamiento
if __name__ == "__main__":
    # Lista de diccionarios de vulnerabilidades de prueba
    vulnerabilities_list = [
        {"id": "CVE-2023-1001", "name": "Reflected XSS", "severity": 6.1},
        {"id": "CVE-2023-2002", "name": "SQL Injection", "severity": 9.8},
        {"id": "CVE-2023-3003", "name": "Information Disclosure", "severity": 3.5},
        {"id": "CVE-2023-4004", "name": "Remote Code Execution", "severity": 9.8},
        {"id": "CVE-2023-5005", "name": "CSRF", "severity": 4.3}
    ]

    # Ejecutar la función
    sorted_list = sort_vulnerabilities(vulnerabilities_list)

    # Imprimir los resultados ordenados de mayor a menor severidad
    print("Vulnerabilidades ordenadas por severidad (mayor a menor):")
    for vuln in sorted_list:
        print(f"[{vuln['severity']}] {vuln['id']} - {vuln['name']}")