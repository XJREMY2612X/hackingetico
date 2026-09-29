# 1. Crear la lista principal usando list()
ports = list()

# 2. Agregar cada elemento (diccionario con puerto y estatus) con .append()
ports.append({"port": 22, "status": "open"})     # Secure Shell (SSH)
ports.append({"port": 80, "status": "open"})     # HTTP
ports.append({"port": 443, "status": "open"})    # HTTPS
ports.append({"port": 21, "status": "closed"})   # FTP
ports.append({"port": 3306, "status": "closed"}) # MySQL

# 3. Lista auxiliar para contar/almacenar los puertos abiertos
counter = list()

# 4. Recorrer la lista para filtrar los puertos abiertos
for p in ports:
    if p["status"] == "open":
        print(f"Port: {p['port']}, Status: {p['status']}")
        counter.append(p)

# 5. Mostrar el total usando len()
print(f"Total Open Ports: {len(counter)}")