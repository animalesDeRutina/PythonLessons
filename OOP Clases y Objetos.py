# POO | Clases y Objetos
# Sintaxis para crear una clase con propiedades y metodos

# ! La propiedad self hace referencia al propio objeto, instancia o ejemplar de la clase


# Creamos clase
class cname():
    # Aqui van las propiedades
    pass

    # Creamos metodo
    def mname(self):
        # Aqui van los metodos
        pass


# Ejemplo:
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


# Accediendo a las propiedades del objeto se utiliza la nomenclatura del punto:

versa = Coche()

print("El coche tiene: ",  versa.llantas, " llantas")

# En el codigo de arriba utilizamos las comas para poder concatenar la propiedad del objeto con el string (texto) si utilizamos un + nos arroja error

# Si queremos cambiar el estado de nuestro coche de estar parado a estar en marcha tenemos que acceder al metodo:

versa.arrancar()

# ¿Que esta ocurriendo? el programa esta leyendo que hay una llamada al metodo.
# Cuando hacemos lo de versa.arrancar() el objeto versa viaja y se almacena en self, de tal forma que cuando le decimos self.enmarcha, realmente lo que le estamos diciendo es: versa.enmarcha = True | cambiando el estado del objeto versa a enmarcha sin alterar la propiedad original de la clase.
if versa.enmarcha == True:
    print("El coche Versa esta en marcha")

else:
    print("El coche Versa no esta en marcha")
# Este condicional IF esta comprobando que si el objeto versa esta en marcha, si lo esta entonces nos imprime "El coche Versa esta en marcha"
