#se importa la libreria random
import random

#se crean 3 variables, que contengan los valores minimos y maximos de los lados y la ultima que permitira la ejecucion del bucle repetidas veces
valor_minimo = 1
valor_maximo = 6
juega_otra_vez = "si"

#se crea el bucle incializando con la variable juega_otra_vez anterior mente
while juega_otra_vez == "si" or juega_otra_vez == "s":
    print("Tirando los dados...")
    print("Los numeros son...")
    #se usa la variable random con el .randint y se complementan con las 2 variables anterior(que escoga un numero anterior entre la variable minimo y maximo)
    print(random.randint(valor_minimo, valor_maximo))
    print(random.randint(valor_minimo,valor_maximo))
    #se le pregunta al usuario si quiere volver a ejecutar o no
    juega_otra_vez = input("¿Desea tirar los dados otra vez?[si/no]: ")