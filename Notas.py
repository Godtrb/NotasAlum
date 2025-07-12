object Alumno
picker=0
while picker !=4:
    print("-----Menu Veterinario-----")
    print("1)Gestion clientes")
    print("2)Gestion mascotas")
    print("3)Citas medicas")
    print("4)Salir")
    picker= int(input("Seleccione una opcion:"))
    match picker:
        case 1: