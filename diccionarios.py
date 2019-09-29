nombreDiccionario = {"España": "Madrid", "Italia": "Roma", "Francia": "Paris"}
print(nombreDiccionario)
print(nombreDiccionario["Italia"])
# El procedimiento para acceder a un dato del diccionario es igual que el
# utilizado para acceder a listas y tuplas.
# Se utiliza una funcion, ya sea print o return (aunque seguro hay mas)
# y entre los parentesis de la funcion se agrega el nombre del diccionario
# y entre corchetes la clave:
# funcion(nombreDiccionario[clave])

# OPERACIONES QUE SE HACEN CON DICCIONARIO


# Agregar un elemento:
#nombreDiccionario [clave] = valor

nombreDiccionario["Mexico"] = "CDMX"
print(nombreDiccionario)
print(nombreDiccionario["Mexico"])

# ! Los diccionarios son case sensitive, lo que quiere decir que no es
# lo mismo Mexico que mexico, si ambas son claves, las claves son independientes

# Eliminar un elemento:
# del nombreDiccionario[clave a eliminar]
# al eliminar una clave del diccionario, su valor por consiguiente tambien
# es eliminado

del nombreDiccionario["Mexico"]
print(nombreDiccionario)

# AHORA VEREMOS UN DICCIONARIO DONDE SE MEZCLAN TIPOS DE VALORES Y CLAVES
diccionarioMezcla = {"Alemania": "Berlin",
                     23: "Edad de Roberto", "fecha de nacimiento Roberto": 1989, "kaliEdad": 1.5, "MateoEdad": 1.5}

print(diccionarioMezcla)

# UTILIZAR UNA TUPLA PARA ASIGNAR CLAVES A LOS VALORES
miTupla = ("España", "Mexico", "Rusia", "Francia", "Italia")
diccionarioDeCapitales = {miTupla[0]: "Madrid", miTupla[1]: "CDMX",
                          miTupla[2]: "Moscu", miTupla[3]: "Paris", miTupla[4]: "Roma"}
print(diccionarioDeCapitales)

# ALMACENAR UNA TUPLA EN UN DICCIONARIO

caracteristicasKalisito = ("bonita", "pelo cafe", "fit", "patitas apestosas")
nuevoDiccionario = {"Alemania": "Berlin",
                    23: "Edad de Roberto", "kalisito": caracteristicasKalisito}
print(nuevoDiccionario["kalisito"])

# 1. Definimos la tupla
# 2. Definimos el diccionario
# 3. Adentro del diccionario creamos una clave X (kalisito) y le asignamos como # valor el nombre de la tupla correspondiente (caracteristicasKalisito)

# METODOS UTILIZABLES CON diccionarios

# Keys
# Este metodo nos arroja las claves del diccionario
print(nombreDiccionario.keys())
# En este caso nos imprimio las claves del diccionario conocido como nombreDiccionario

# Values
# Este metodo nos arroja los valores del diccionarios
print(nombreDiccionario.values())
# En este caso nos imprimio las claves del diccionario conocidoc como nombreDiccionario

# Len
# Este metodo nos arroja la longitud de un cierto diccionario, la longitud de sus valores
print(len(nombreDiccionario))
# En este caso nos imprime la longitud de valores de nombreDiccionario
