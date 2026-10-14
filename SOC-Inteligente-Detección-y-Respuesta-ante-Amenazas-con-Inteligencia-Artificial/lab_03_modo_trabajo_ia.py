# ==============================================================================
# Archivo:       lab_03_modo_trabajo_ia.py
# Autor:         Maurice Victor Frayssinet Delgado
# Fecha:         12-10-2026
# Curso:         Fundamentos de Inteligencia Artificial
# Descripción:   Implementación de un modelo de lenguaje generativo básico
#                basado en Cadenas de Markov. Simula la fase de entrenamiento
#                sobre un corpus de texto para construir una matriz de transición
#                (probabilidades de secuencias de palabras) y demuestra la
#                generación autorregresiva (predicción del siguiente token) paso
#                a paso hasta encontrar un token de parada (.).
# Versión:       1.0
# Dependencias:  random, time
# ==============================================================================
import random
import time

# 1. Datos de entrenamiento (lo que el modelo "lee" para aprender el mundo)
corpus = [
    "un gato es un felino que caza ratones .",
    "un gato es un animal domestico muy limpio .",
    "un gato toma leche y duerme en el sofa .",
    "el gato maulla cuando tiene hambre ."
]

# 2. Fase de entrenamiento: Aprender qué palabra sigue a cuál
modelo_probabilidades = {}

for oracion in corpus:
    tokens = oracion.split()
    for i in range(len(tokens) - 1):
        palabra_actual = tokens[i]
        palabra_siguiente = tokens[i + 1]

        if palabra_actual not in modelo_probabilidades:
            modelo_probabilidades[palabra_actual] = []
        modelo_probabilidades[palabra_actual].append(palabra_siguiente)

print("=" * 65)
print("PASO 1: MODELO ENTRENADO (MATRIZ DE TRANSICIÓN)")
print("=" * 65)
for origen, destinos in modelo_probabilidades.items():
    print(f"Tras '{origen}' suele venir: {destinos}")

# 3. Generación autorregresiva (token por token)
def generar_texto(palabra_inicial, max_palabras=10):
    frase = [palabra_inicial]
    palabra_actual = palabra_inicial

    print("\n" + "=" * 65)
    print(f"PASO 2: GENERACIÓN AUTORREGRESIVA (Inicio: '{palabra_inicial}')")
    print("=" * 65)

    paso = 1
    while paso < max_palabras:
        opciones = modelo_probabilidades.get(palabra_actual)

        if not opciones:
            print(f"Paso {paso}: No hay más continuaciones posibles.")
            break

        # Calcular porcentaje de cada opción
        total_opciones = len(opciones)
        conteo = {p: opciones.count(p) for p in set(opciones)}
        distribucion = {p: f"{(cant / total_opciones)*100:.1f}%" for p, cant in conteo.items()}

        # El modelo elige la siguiente palabra (aquí toma una según su frecuencia)
        palabra_elegida = random.choice(opciones)

        print(f"\n[Paso {paso}] Contexto actual: {' '.join(frase)}")
        print(f"  Candidatos posibles: {distribucion}")
        print(f"  -> Palabra seleccionada: '{palabra_elegida}'")

        frase.append(palabra_elegida)
        palabra_actual = palabra_elegida

        if palabra_actual == ".":
            print("\n[Fin detectado: Se generó el token de parada '.']")
            break

        paso += 1

    return " ".join(frase)

# --- CORRIDA ---
# Le damos un "prompt" inicial:
prompt = "un"
resultado_final = generar_texto(prompt)

print("\n" + "=" * 65)
print("TEXTO FINAL SINTETIZADO POR LA IA:")
print("=" * 65)
print(f"\"{resultado_final}\"")