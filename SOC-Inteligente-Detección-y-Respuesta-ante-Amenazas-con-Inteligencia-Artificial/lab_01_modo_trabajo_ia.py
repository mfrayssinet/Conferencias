# ==============================================================================
# Archivo:       lab_01_modo_trabajo_ia.py
# Autor:         Maurice Victor Frayssinet Delgado
# Fecha:         12-10-2026
# Curso:         Fundamentos de Inteligencia Artificial
# Descripción:   Demostración introductoria de cómo un sistema de IA procesa
#                lenguaje natural. Convierte cadenas de texto en vectores
#                numéricos (frecuencia de palabras) y utiliza la métrica de
#                similitud del coseno para encontrar la respuesta más afín
#                dentro de una base de conocimiento predefinida.
# Versión:       1.0
# Dependencias:  math
# ==============================================================================
import math

# 1. Base de conocimiento: preguntas y respuestas
base_datos = {
    "que es un gato": "Un felino domestico que maulla y caza ratones.",
    "que es un perro": "Un canino domestico conocido como el mejor amigo del hombre.",
    "que es un auto": "Un vehiculo terrestre de cuatro ruedas a motor."
}

# 2. Vocabulario: asignamos a cada palabra un indice numerico
vocabulario = ["que", "es", "un", "gato", "perro", "auto"]

# 3. Vectorizacion: convertir una frase en una lista de numeros (vector)
def texto_a_vector(texto):
    palabras = texto.lower().split()
    return [palabras.count(palabra) for palabra in vocabulario]

# 4. Calculo matematico: similitud de coseno entre dos vectores numericos
def calcular_similitud(vec1, vec2):
    producto_punto = sum(a * b for a, b in zip(vec1, vec2))
    norma1 = math.sqrt(sum(a * a for a in vec1))
    norma2 = math.sqrt(sum(b * b for b in vec2))
    return producto_punto / (norma1 * norma2) if norma1 and norma2 else 0.0

# --- SIMULACION ---
pregunta_usuario = "que es gato"

# La IA solo ve esto:
vector_pregunta = texto_a_vector(pregunta_usuario)
print(f"Pregunta como numeros: {vector_pregunta}\n")

mejor_puntuacion = -1
mejor_respuesta = ""

# El modelo compara numeros contra numeros
for pregunta_registrada, respuesta in base_datos.items():
    vector_registrado = texto_a_vector(pregunta_registrada)
    similitud = calcular_similitud(vector_pregunta, vector_registrado)
    print(f"Comparando con '{pregunta_registrada}' -> Similitud: {similitud:.3f}")

    if similitud > mejor_puntuacion:
        mejor_puntuacion = similitud
        mejor_respuesta = respuesta

print(f"\nRespuesta seleccionada:\n\"{mejor_respuesta}\"")