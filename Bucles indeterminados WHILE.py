
# Bucles Indeterminados | WHILE
import math

# Los bucles WHILE pueden ser determinados si se usa un marcador
# ejemplo:

marcador = 1
while marcador <= 10:
    print("el marcador es menor a diez")
    print("el marcador es " + str(marcador))
    marcador = marcador + 1

# Utilizando la caracteriztica indeterminada del bucle:
# En este ejemplo haremos lo del ejemplo de los indeterminados anteriores, solo # que esta vez le pedirá al usuario que introduzca su edad. Si el usuario
# introduce un dato negativo le arrojará un error. Así hasta que arroje un dato # positivo, si el usuario ingresa mil datos negativos el bucle se repetirá mil # veces.

edad = int(input("Edad: "))
intentos = 1
while edad <= 0:
    print("Has introducido una edad negativa")
    print("intento No. " + str(intentos))
    intentos = intentos + 1
    edad = int(input("Vuelve a introducir tu edad: "))

print("Has introducido tu edad correctamente")
print("La edad introducida es " + str(edad))

# Hay veces que es necesario que el bucle que tenemos no se convierta en uno infinito, para eso tambien nos ayuda el contador de intentos agregado en el codigo. En el siguiente ejemplo veremos la funcion de importar, que es para importar clases. Se hara un codigo que calcule la raiz cuadrada de un numero - código del ejemplo del tutorial bucles IV video 17 minuto 14  -
numero = int(input(" Dame un numero: "))
intentos = 0
while numero < 0:
    print("No se puede hayar la raiz de un numero negativo")

    if intentos == 2:
        print("Has consumido demasiados intentos, el programa se cerrara")
    break
    numero = int(input(" Dame un numero: "))
if numero < 0:
    intentos = intentos + 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print("la raiz cuadrada de " + str(numero) + " es: " + str(solucion))

# Instrucciones adicionales que se pueden utilizar en bucles | Continue, pass y else

# Continue
# Esta instrucción salta a la siguiente interaccion de bucle, si tenemos un bucle que darà diez vueltas y cuando esta en la vuelta 5 lee esta instrucciòn e ignora esa vuelta de bucle a partir de la lectura de la instruccion y pasaria a la vuelta 6.

# Pass
# Esta instruccion se suele usar mucho cuando defines clases y de momento esa clase necesitas que sea una clase nula. Devuelve null en cuanto se lee en el interior de un bucle, al devolver null es como si no se ejecutará el bucle. O cuando como desarrollador necesitas un bucle pero dejas el desarrollo de este al final. Asi el programa “no ejecuta” el bucle vacío y el programa corre normal

# Else
# Esta instrucción funciona de forma muy similar a como lo hace dentro de un condicional. El sentido del else dentro de un bucle for o un bucle whille tiene la misma funcion que el else de un condicional IF

# Ejemplos:

# Continue
for letra in "Python":
    if letra == "h":
        continue

# Esto quiere decir que cuando letra se encuentre con la h ignora el print y se salta a la siguiente vuelta que es para leer la o.

    print("Viendo la letra: " + letra)

# Pass

# Uilidad 1 | crear una clase vacia para llenarla después sin generar errores


class nombreClase:
    pass

# Uilidad 2 | crear una funcion vacia para después meterle instrucciones


def miFuncion():
    pass
