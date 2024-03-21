import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de fallos permitidos
max_fails = 10
# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print(f"Estoy pensando en una palabra. ¿Puedes adivinar cuál es? Tu maximo de fallos es de {max_fails}")
print("""Ingrese el numero de dificultad que desea jugar
        1: Fácil (se le mostrarán  todas las vocales de la palabra)
        2: Medio (se le mostrarán la primera y última letra de la palabra)
        3: Difícil (NO se le mostrará ninguna letra de la palabra)
""")

level=input("Dificultad: ")
match level:
    case "1":
        word_displayed=""
        print("Modo fácil")
        for car in secret_word:
            if car in "aeiouó":
                word_displayed=word_displayed + car
            else:
                word_displayed=word_displayed+"_"
    case "2":
        print("Modo medio")
        word_displayed=secret_word[0]+ "_" *(len(secret_word)-2) + secret_word[-1]
    case "3":
        print("Modo difícil")
        word_displayed = "_" * len(secret_word)
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

fails=0
while fails < max_fails:
     # Pedir al jugador que ingrese una letra
     letter = input("Ingresa una letra: ").lower()
     # Verificar que el valor de la letra no sea un string vacio o ya haya sido adivinada
     if(letter==""):
         print("Valor invalido, por favor ingrese otro")
         continue
     elif letter in guessed_letters:
         print("Ya has intentado con esa letra. Intenta con otra.")
         continue
     # Agregar la letra a la lista de letras adivinadas
     guessed_letters.append(letter)
     # Verificar si la letra está en la palabra secreta
     if letter in secret_word:
         print("¡Bien hecho! La letra está en la palabra.")
     else:
         fails=fails+1
         print(f"Lo siento, la letra no está en la palabra. Llevas {fails} fallos")
     # Mostrar la palabra parcialmente adivinada
     letters = []
     for letter in secret_word:
         if letter in guessed_letters:
             letters.append(letter)
         else:
             letters.append("_")
     match level:
        case "1":
            word_displayed = "".join([letter if letter in "aeiouó" or letter in guessed_letters else "_" for letter in secret_word]) 
        case "2":
            word_displayed = secret_word[0] + "".join([letter if letter in guessed_letters else "_" for letter in secret_word[1:-1]]) + secret_word[-1]
        case "3":
            word_displayed = "".join(letters)
     print(f"Palabra: {word_displayed}")
     # Verificar si se ha adivinado la palabra completa
     if word_displayed == secret_word:
         print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
         break
else:
     print(f"¡Oh no! Has agotado tus {max_fails} fallos.")
     print(f"La palabra secreta era: {secret_word}")