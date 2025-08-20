import re

texto = """
Log del sistema - 20/08/2025

Conexión establecida desde 192.168.0.1 hacia el servidor central.
El cliente en 10.10.10.10 reportó un error de autenticación.
Reintento automático desde 172.16.5.4 con éxito.
Se detectó un acceso sospechoso desde 300.45.23.9 (IP inválida).
DNS público consultado: 8.8.8.8 y 1.1.1.1.
Otro intento fallido desde 192.168.100.256 (IP inválida).
Cliente móvil conectado desde 100.64.0.15.
Servidor de respaldo: 192.0.2.123.
IPv6 visto: 2001:db8:85a3:0000:0000:8a2e:0370:7334
"""

# Patrón simple: cualquier número de 1 a 3 dígitos separado por puntos
patron_simple = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

ips = re.findall(patron_simple, texto)
print("Direcciones IP encontradas:")
for ip in ips:
    print("-", ip)
