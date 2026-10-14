# ============================================================
# LABORATORIO DE CIBERSEGURIDAD - ANALISIS DE LOGS
# Autor       : Maurice Frayssinet
# Fecha       : 14/10/2026
# Programa    : lab_02_laya.py
# Descripcion : Detección de direcciones IP sospechosas.
# ============================================================
"""Ejercicio educativo con eventos sintéticos. No ejecuta acciones de bloqueo."""

import csv
import json
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timedelta

BASE = Path(__file__).resolve().parent
LOG = BASE / "eventos_demo.csv"

def cargar():
    if not LOG.exists():
        crear_demo()
    with LOG.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def crear_demo():
    filas = []
    inicio = datetime(2026, 10, 14, 8, 0)
    for i in range(120):
        tipo = ["login_ok", "login_fail", "firewall_deny", "web_request", "port_connection"][i % 5]
        ip = "203.0.113.25" if i % 7 == 0 else f"192.0.2.{(i % 15) + 1}"
        detalle = "normal"
        if tipo == "web_request" and i % 3 == 0: detalle = "GET /?id=1 UNION SELECT password FROM users"
        if tipo == "port_connection": detalle = f"dst_port={20 + i}"
        if tipo == "firewall_deny": detalle = "blocked tcp connection"
        filas.append(dict(timestamp=(inicio + timedelta(minutes=i*8)).isoformat(), ip=ip, usuario=f"user{i%8}", evento=tipo, detalle=detalle))
    for j in range(15):
        filas.append(dict(timestamp=(inicio+timedelta(minutes=j)).isoformat(),ip="198.51.100.77",usuario="admin",evento="login_fail",detalle="bad password"))
    for j in range(30):
        filas.append(dict(timestamp=(inicio+timedelta(seconds=j*10)).isoformat(),ip="198.51.100.88",usuario="-",evento="port_connection",detalle=f"dst_port={1000+j}"))
    with LOG.open("w", encoding="utf-8", newline="") as f:
        w=csv.DictWriter(f, fieldnames=["timestamp","ip","usuario","evento","detalle"]); w.writeheader(); w.writerows(filas)
    print("Dataset de demostración creado:", LOG)

if __name__ == "__main__":
    eventos=cargar()
    puntajes=Counter()
    for e in eventos:
        puntajes[e["ip"]] += {"login_fail":3,"firewall_deny":2,"port_connection":1}.get(e["evento"],0)
    for ip, puntos in puntajes.most_common(10): print(f"{ip}: riesgo heurístico={puntos}")
