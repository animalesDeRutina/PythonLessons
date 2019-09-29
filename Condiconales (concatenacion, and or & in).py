# MAS OPCIONES DE CONDICIONALES

# Concatenación de operadores de comparacion
# Codigo del tutorial - condiconales III -
edad = - 7

if edad < 100:
    print("edad correcta")

else:
    print("edad es incorrecta")

# El problema empieza cuando nuestro valor es negativo, porque se cumple la
# condicion, menos siete es menor a cien por lo tanto imprime "edad es correcta"
# Este problema tiene solucioon usando if, elif, pero para abreviar codigo
# utilizaremos la concatenación de operadores de comparacion para hacerlo
# utilizaremos varias veces el operador de comparacion dentro de la misma
# condicion del if utilizar varias veces el operacion de comparacion

# edad = - 7

# if 0 < edad < 100:
    # print("edad correcta")

# else:
    # print("edad es incorrecta")

# Aqui entonces habriamos colocado parametros a edad, debe ser mayor a 0
# pero menor a 100 para que nos imprima "edad es correcta"

edad = 7

if edad < 100:
    print("edad es correcta")

else:
    print("edad es incorrecta")

# Uso de operadores lógicos AND & OR
# Para este crearemos un programa que evalue si un alumno tiene beca o no
# Codigo del video - Condicinales IV -
# este programa va a evaluar lo siguente
# - distacia que recorre el alumno al ir a la escuela
# - Si el alumno tiene hermanos en la misma escuela > 2
# - Salario familiar <= 20000
# Se les dara beca a los que complan los tres

# Utilizando AND
distanciaEscuela = int(input("A que distancia estas de la escuela en km "))
print(distanciaEscuela)

numeroHermanos = int(input("Cuantos heramnos hay en el centro "))
print(numeroHermanos)

salarioFamiliar = int(input("Cuanto gana tu familia al año "))
print(salarioFamiliar)

if distanciaEscuela > 40 and numeroHermanos > 2 and salarioFamiliar <= 20000:
    print("tienes derecho a beca")

else:
    print("no tienes derecho a beca")


# Utilizando OR

distanciaEscuela = int(input("A que distancia estas de la escuela en km "))
print(distanciaEscuela)

numeroHermanos = int(input("Cuantos heramnos hay en el centro "))
print(numeroHermanos)

salarioFamiliar = int(input("Cuanto gana tu familia al año "))
print(salarioFamiliar)

if distanciaEscuela > 40 and numeroHermanos > 2 or salarioFamiliar <= 20000:
    print("tienes derecho a beca")

else:
    print("no tienes derecho a beca")

# Utilizando IN
# Programa para un usuario que tomara una optativa y de la que no puede
# librarse

print("asignaturas: Mate, Fisica, Python")
asignatura = input("Elige tu asignatura ")

if asignatura in ("asignaturas: Mate, Fisica, Python"):
    print("Asigantura elegida " + asignatura)

else:
    print("la asigantura " + asignatura + " no esta en las opciones")
