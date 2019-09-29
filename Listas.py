# Listas
# Pagina 1

miLista = ["Maria", "Pepe", "Marta", "Antonio"]

# FROMAS DE ACCEDER A LA INFORMACIÓN DENTRO DE UNA LISTA

print(miLista[0])
# esta linea de codigo nos arrojaria como resultado Maria,
# pues estamos imprimiendo en consola mediante el indice
# el primer elemento de la lista

print(miLista[:])
# esta linea de codigo nos arrojaria como resultado
# toda la lista

print(miLista[-3])
# Cuando intentamos acceder a un dato de nuestra
# lista con un valor negativo la lista en cuestion
# toma entonces como punto de partida el final y nos da
# el numero de elementos a la izquierda que nosotros
# especificamos tomando ahora si como punto de partida el
# indice 1 en el ultimo elemento

print(miLista[0:3])
# Esto le dice a la lista que debe imprimir los
# tres primeros elementos de la lista

print(miLista[2:])

# Esto hace que imprima en la consola a
# partir del indice 2 hasta el final de la lista

# _______________________________________________________________________________

# FUNCIONES PREDEFINIDAS QUE ALTERAN LAS LISTAS

# append - esta función nos permite agregar
# un nuevo elemento a la lista al final de la misma.
# su sintaxis es:
# nombreDeLaLista.append(elemento a agregar)

# insert - esta función nos permite agregar
# un nuevo elemento a la lista en un punto
# que definiremos con un indice.
# su sintaxis es:
# nombreDeLaLista.insert(indice + coma elemento a agregar)

# extend - esta funcion nos permite agregar una serie de nuevos
# elementos a la lista al final de los elementos anteriores
# su sintaxis es:
# nombreDeLaLista.extend([elementos que queremos agregar separados por comas])
# este es basicamente encadenar dos listas juntas

# index - esta funcion nos dice en que indice esta cierto elemento de la lista
# su sintaxis es:
# nombreDeLaLista.index(elemento)
# normalmente es utilizada en una funcion print o return

# in - Este elemento nos arroja un boolean de true o false para indicarnos si
# el elemento que hemos puesto esta dentro de la lista seleccionada
#! Este elemento es utilizado en una función return o print
# su sintaxis es:
# print(elemento + in + nombre de la lista)

# remove - Esta funcion permite eliminar un elemento de la lista
# su sintaxis es:
# nombreDeLaLista.remove(elemento a eliminar)

# pop - Esta funcion permite eliminar el ultimo elemento de una lista
# su sintaxis es:
# nombreDeLaLista.pop()
