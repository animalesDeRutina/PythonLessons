# Condicionales
# Este trozo de codigo es igual al del tutorial que tenemos descargado sobre
# condicionales, - condicionales I - por si necesitamos consultar informacion

notaAlumno = int(input("Define nota de alumno "))


def evaluacionAlumno(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "suspenso"
    return valoracion


print(evaluacionAlumno(notaAlumno))

# Condicionales usando if, else y elif
# Vamos a hacer u programa que le diga al usuario mediante un inpt de su
# edad si es viejo, joven o si esta muerto.
# Para hacerlo le pediremos un input de su edad y utilizaremos las Condicionales
# Para arrojar alguna de las tres opciones

edadUsuario = int(input("Dime tu edad "))

if edadUsuario <= 40:
    print("eres joven, de que te preocupas")

elif edadUsuario >= 100:
    print("estas muerto, yo no soy la ouija")


else:
    print("ya estas un poco viejo")

# ! Elif debe ir siempre entre if y else nunca abajo, nunca arriba
