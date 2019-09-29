# Funciones
# Pagina 1


def nombreUsuario(nombreUsuario):
    print("Hola " + nombreUsuario)


nombreUsuario("Eduardo")
nombreUsuario("Enrique")

# Pagina 2

# Esta es una función de tipo 1
# Ejecuta una acción, en este caso esta función imprime en consola
# el mensaje de -Hi Eduardo-


def greet(name):
    print("Hi " + name)


greet("Eduardo")

# Esta es una funcion de tipo 2
# Guarda en una variable el dato resultado de la ejecucion de la función para su
# uso posterior


def greet(name):
    return "Hi " + name


variable1 = greet("Eduardo")
