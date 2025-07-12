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
            return 1
        elif NotFin <0 |NotFin>100:
            print("Nota invalida.")
    elif carne<0:
        print("Carne invalido.")
def infoalumn (Alumno):
    print("Nombre: ",Alumno.nombre)
    print("Carne: ",Alumno.carne)
    print("Carrera: ",Alumno.Carrera)
    print("Nota final: ",Alumno.Nota_Final)
def AlumSearch (ListAlum=[]):
    found=0
    AlumPicker=int(input("Ingrese el carne del alumno a buscar:"))
    if AlumPicker>0:
        for alum in ListAlum:
            if alum.carne==AlumPicker:
                infoalumn(alum)
                found=1
    elif AlumPicker<0:
        print("Carne invalido.")
        if found==0:
            print("Alumno no encontrado.")

picker=0
alumsthere=0
ListAlum=[]
while picker !=4:
    print("-----Menu Notas-----")
    print("1)Registrar nuevo alumno")
    print("2)Buscar alumno por carne")
    print("3)Verificar promedio")
    print("4)Salir")
    picker= int(input("Seleccione una opcion:"))
    match picker:
        case 1:
            alumsthere=AlumnoReg(ListAlum)
        case 2:
            if alumsthere==0:
                print("No hay alumnos encontrados")
            elif alumsthere==1:
                AlumSearch(ListAlum)
        case 3:
            if alumsthere==0:
                print("No hay alumnos encontrados")
            elif alumsthere==1:
