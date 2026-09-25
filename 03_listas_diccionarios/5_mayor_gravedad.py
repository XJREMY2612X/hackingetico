# 5. Mayor gravedad primero[cite: 11]
vulns = [
    {"title": "Info Leak", "severity": 3},
    {"title": "RCE", "severity": 10},
    {"title": "XSS", "severity": 6}
]

vulns_ordenadas = sorted(vulns, key=lambda x: x.get("severity", 0), reverse=True)
print("Ordenadas por gravedad:", vulns_ordenadas)
