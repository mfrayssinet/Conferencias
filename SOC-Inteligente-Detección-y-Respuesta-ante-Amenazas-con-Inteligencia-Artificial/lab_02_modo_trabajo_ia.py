# ==============================================================================
# Archivo:       lab_02_modo_trabajo_ia.py
# Autor:         Maurice Victor Frayssinet Delgado
# Fecha:         12-10-2026
# Curso:         Fundamentos de Inteligencia Artificial
# Descripción:   Versión de trazabilidad (caja blanca) del motor de similitud
#                de texto. Desglosa en consola las operaciones matemáticas
#                internas de la IA: mapeo del vocabulario base, cálculo del
#                producto punto par a par, cálculo de normas (magnitudes) y
#                la obtención del porcentaje de coincidencia de similitud del
#                coseno para la toma de decisiones.
# Versión:       1.0
# Dependencias:  math
# ==============================================================================
import math

# 1. Base de conocimiento
base_datos = {
    "que es un gato": "Un felino domestico que maulla y caza ratones.",
    "que es un perro": "Un canino domestico conocido como el mejor amigo del hombre.",
    "que es un auto": "Un vehiculo terrestre de cuatro ruedas a motor."
}

# 2. Diccionario o vocabulario base (posiciones 0 a 5)
vocabulario = ["que", "es", "un", "gato", "perro", "auto"]

print("=" * 65)
print("PASO 1: VOCABULARIO BASE (MAPA DE PALABRAS A COORDENADAS)")
print("=" * 65)
for indice, palabra in enumerate(vocabulario):
    print(f"  Posición {indice} -> '{palabra}'")

# 3. Función de vectorización con trazabilidad
def texto_a_vector(texto, etiqueta=""):
    palabras = texto.lower().split()
    vector = [palabras.count(p) for p in vocabulario]
    if etiqueta:
        print(f"\n[Vectorización] {etiqueta}: \"{texto}\"")
        print(f"  Palabras detectadas: {palabras}")
        print(f"  Vector resultante  : {vector}")
    return vector

# 4. Función de similitud matemática con detalle de operaciones
def calcular_similitud_detallada(vec_pregunta, vec_candidato, nombre_candidato):
    print(f"\n--- Comparando con: \"{nombre_candidato}\" ---")
    print(f"  Vector pregunta   : {vec_pregunta}")
    print(f"  Vector candidato  : {vec_candidato}")

    # Producto punto: multiplicar posición por posición y sumar
    multiplicaciones = [p * c for p, c in zip(vec_pregunta, vec_candidato)]
    producto_punto = sum(multiplicaciones)
    print(f"  Multiplicación par a par: {multiplicaciones}")
    print(f"  Producto punto (suma)   : {producto_punto}")

    # Normas (magnitud de cada vector)
    norma_p = math.sqrt(sum(p * p for p in vec_pregunta))
    norma_c = math.sqrt(sum(c * c for c in vec_candidato))
    print(f"  Longitud vector pregunta : √{sum(p*p for p in vec_pregunta)} = {norma_p:.4f}")
    print(f"  Longitud vector candidato: √{sum(c*c for c in vec_candidato)} = {norma_c:.4f}")

    # Similitud de coseno: producto punto / (norma_p * norma_c)
    similitud = producto_punto / (norma_p * norma_c)
    print(f"  Cálculo final: {producto_punto} / ({norma_p:.4f} * {norma_c:.4f})")
    print(f"  -> Puntuación de similitud: {similitud:.4f} ({similitud * 100:.1f}%)")
    return similitud

# --- CORRIDA DEL PROGRAMA ---
pregunta_usuario = "que es gato"

print("\n" + "=" * 65)
print("PASO 2: CONVERTIR LA ENTRADA DEL USUARIO A NÚMEROS")
print("=" * 65)
vector_usuario = texto_a_vector(pregunta_usuario, "Entrada del usuario")

print("\n" + "=" * 65)
print("PASO 3: COMPARACIÓN MATEMÁTICA CON CADA OPCIÓN EN MEMORIA")
print("=" * 65)

mejor_puntuacion = -1
mejor_respuesta = ""
mejor_pregunta = ""

for pregunta_registrada, respuesta in base_datos.items():
    vector_registrado = texto_a_vector(pregunta_registrada)
    similitud = calcular_similitud_detallada(vector_usuario, vector_registrado, pregunta_registrada)

    if similitud > mejor_puntuacion:
        mejor_puntuacion = similitud
        mejor_respuesta = respuesta
        mejor_pregunta = pregunta_registrada

print("\n" + "=" * 65)
print("PASO 4: DECISIÓN DEL MODELO (MÁXIMA PROBABILIDAD / SIMILITUD)")
print("=" * 65)
print(f"Opción ganadora : \"{mejor_pregunta}\" con {mejor_puntuacion * 100:.1f}% de coincidencia.")
print(f"Respuesta final enviada al usuario:\n\"{mejor_respuesta}\"")