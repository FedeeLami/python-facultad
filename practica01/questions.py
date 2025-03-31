import random
import sys

# Lista de preguntas con sus opciones de respuesta y la respuesta correcta
data = [
    ("¿Qué función se usa para obtener la longitud de una cadena en Python?", ("size()", "len()", "length()", "count()"), "len()"),
    ("¿Cuál de las siguientes opciones es un número entero en Python?", ("3.14", "'42'", "10", "True"), "10"),
    ("¿Cómo se solicita entrada del usuario en Python?", ("input()", "scan()", "read()", "ask()"), "input()"),
    ("¿Cuál de las siguientes expresiones es un comentario válido en Python?", ("// Esto es un comentario", "/* Esto es un comentario */", "-- Esto es un comentario", "# Esto es un comentario"), "# Esto es un comentario"),
    ("¿Cuál es el operador de comparación para verificar si dos valores son iguales?", ("=", "==", "!=", "==="), "==")
]

# Seleccionar 3 preguntas sin repetir
questions_to_ask = random.sample(data, 3)

puntuacion = 0

for question, options, correct_answer in questions_to_ask:
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    for intento in range(2):
        user_answer = input("Respuesta: ")
        
        if not user_answer.isdigit() or not (1 <= int(user_answer) <= len(options)):
            print("Respuesta no válida")
            sys.exit(1)

        chosen_answer = options[int(user_answer) - 1]
        
        if chosen_answer == correct_answer:
            print("¡Correcto!")
            puntuacion += 1
            break
        else:
            print("Incorrecto")
            if puntuacion >= 0.5:
                puntuacion -= 0.5
            if intento == 1:
                print(f"La respuesta correcta era: {correct_answer}")
    print()

print(f"Tu puntuación final fue: {puntuacion}")
