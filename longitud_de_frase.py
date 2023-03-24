# Introduce una palabra de 4 a 8 letras
# 1. Si la longitud de la palabra se encuentra en el limite de 4 a 8 arrojar mensaje de que la palabra es correcta.
# 2. Si la longitud de la palabra es menor a 4 digitos, arrojar mensaje de que se necesita de 4 a 8 caracteres.
# 3. Si la longitud rebasa los 8 caracteres, arrojar mensaje de que se exedio en letras. 

palabra = input("Ingresa una palabra de 4 a 8 caracteres: ")
caracteres = len (palabra)
tipo = palabra.isalnum()

contador=0

for i in palabra:
    contador+=1

if tipo == True:
    if caracteres < 4:
        print("La palabra tiene", len(palabra), "caracteres y se requiere un minimo 4.")
    elif caracteres > 8:
        print("La palabra tiene", len(palabra), "caracteres y debe tener maximo 8.")
    else:
        print("La palabra es correcta")