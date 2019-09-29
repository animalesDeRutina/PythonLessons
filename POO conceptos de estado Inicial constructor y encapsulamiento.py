# POO | Clases y Objetos
# Conceptos: ESTADO INICIAL, CONSTRUCTOR Y ENCAPSULAMIENTO

# Para mayor facilidad reutilizamos la clase de la hoja de codigo anterior


class Coche():
    llantas = 4
    espejos = 3
    motor = True
    tanque = True
    # ! La propiedad enMarcha nos dice si el coche esta en marcha o detenido, al ser false en principio todos los coches estaeran detenidos
    enmarcha = False

# ! Este metodo hara que nuesto coche pase de estar detenido a estar en marcha
    def arrancar(self):
        self.enmarcha = True


tsuru = Coche()

# Finalmente si imprimimos en consola las caracteristicas del segundo objeto que hemos creado estas se mantienen igual, pues las propiedades pese a que este sea un coche nuevo se mantienen.

print("El coche tiene: ",  tsuru.llantas, " llantas")

# CONSTRUCTOR Y ESTADO INICIAL


# El codigo de abajo funciona igual que el de arriba solo que el de abajo tiene un estado inicial

class Coche():
    def __init__(self):
        self.llantas = 4
        self.espejos = 3
        self.motor = True
        self.tanque = True
        self.enmarcha = False

    def arrancar(self):
        self.enmarcha = True


tsuru = Coche()


print("El coche tiene: ",  tsuru.llantas, " llantas")


# CONSTRUCTOR Y ESTADO INICIAL Y ENCAPSULAMIENTO


class Coche():
    def __init__(self):
        self.llantas = 4
        self.espejos = 3
        self.motor = True
        self.tanque = True
        self.enmarcha = False

    def arrancar(self):
        self.enmarcha = True


tsuru = Coche()

# Si yo antes de pedir que imprima la catidad de llantas que tiene el objeto TSURU a la consola cambiamos el numero de llantas que tiene el objetio TSURU

# el codigo:
# tsuru.llantas = 10
# Modifica la propiedad de llantas del TSURU a 10

tsuru.llantas = 10

print("El coche tiene: ",  tsuru.llantas, " llantas")

# Para evitar que se puedan cambiar las propiedades de una clase al llamar a la clase necesitamos ENCAPSULAR estas propiedades, para hacerlo antes de su nombre ponemos dos guiones bajos

# class Coche():
# def __init__(self):
# self.__llantas = 4
# self.espejos = 3
# self.motor = True
# self.tanque = True
# self.enmarcha = False

# Ahora la propiedad LLANTAS esta encapsulada y esta no puede ser modificidada desde fuera de la clase. Sin embargo, desde dentro si nosotros queremos modificarla si se podria.

# ! Tambien los metodos se pueden encapsular:

# class Coche():
# def __init__(self):
# self.llantas = 4
# self.espejos = 3
# self.motor = True
# self.tanque = True
# self.enmarcha = False

# def arrancar(self):
# self.__enmarcha = True
