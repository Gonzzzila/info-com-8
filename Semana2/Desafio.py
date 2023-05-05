texto = input("Ingresa un texto: ")
letras = input("Ingresa 3 letras separadas por comas: ")
letras = letras.lower().split(',')

#Cuenta la cantidad de veces que aparece cada letra y lo muestra.
cantidad_letras = {letra: texto.lower().count(letra) for letra in letras}
print("Cantidad de veces que aparece cada letra:", cantidad_letras)

#Cuenta la cantidad total de palabras en el texto y lo muestra.
palabras = texto.split()
cantidad_palabras = len(palabras)
print("Cantidad de palabras en el texto:", cantidad_palabras)

#Muestra la primera y última letra del texto.
primera_letra = texto[0]
ultima_letra = texto[-1]
print("Primera letra:", primera_letra)
print("Última letra:", ultima_letra)

#Realiza el texto inverso.
texto_inverso = texto[::-1]
print("Texto en orden inverso:", texto_inverso)

#Revisa si la palabra "python" aparece en el texto y dice si es verdadero o no.
aparece_python = "python" in palabras
print("¿Aparece la palabra 'python'?", aparece_python)