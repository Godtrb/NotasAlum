class Alumno:

    def __init__(self, nombre, carne,Carrera,Nota_Final):
        self.nombre = nombre
        self.carne = carne
        self.Carrera = Carrera
        self.Nota_Final = Nota_Final

def AlumnoReg(ListAlumn=[]):
    name = input("Ingres el nombre del alumno:")
    carne = int(input("Ingrese el carne del alumno"))
    if carne>0:
        Carrera=input("Ingrese la carrera del alumno:")
        NotFin=int(input("Ingrese la nota final del alumno:"))
        if (NotFin>=1|NotFin<=100):
            newalumn=Alumno(name,carne,Carrera,NotFin)
            ListAlumn.append(newalumn)
        elif NotFin <0 |NotFin>100:
            print("Nota invalida.")

picker=0
while picker !=4:
    print("-----Menu Veterinario-----")
    print("1)Registrar nuevo alumno")
    print("2)Gestion mascotas")
    print("3)Citas medicas")
    print("4)Salir")
    picker= int(input("Seleccione una opcion:"))
    match picker:
        case 1:
