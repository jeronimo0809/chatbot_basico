from transformers import pipeline

# Crear el chatbot
chatbot = pipeline("text-generation", model="distilgpt2")

# Contexto que el chatbot usará
contexto = """
El Colegio ABC fue fundado en 1995.
La mascota del colegio es un águila.
El colegio tiene estudiantes desde preescolar hasta grado 11.
El color oficial del colegio es azul.
"""

print("🤖 Chatbot con contexto listo.")
print("Escribe 'salir' para terminar.\n")

while True:

    pregunta = input("Tú: ")

    if pregunta.lower() == "salir":
        print("🤖 Adiós!")
        break

    # Crear prompt con contexto
    prompt = f"""
    Usa la siguiente información para responder la pregunta.

    Información:
    {contexto}

    Pregunta:
    {pregunta}

    Respuesta:
    """

    respuesta = chatbot(
        prompt,
        max_length=120,
        num_return_sequences=1
    )

    texto = respuesta[0]["generated_text"]

    # Separar solo la respuesta
    respuesta_final = texto.split("Respuesta:")[-1]

    print("\n🤖", respuesta_final.strip())
    print()
