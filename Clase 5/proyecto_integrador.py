usuario = "admin"
contrasena = "uni123"
ingresar_usuario = input("Ingrese su usuario: ")
ingresar_contrasena = input("Ingrese su contraseña: ")

alumnos = []

if ingresar_usuario == usuario and ingresar_contrasena == contrasena:
    print("Bienvenido")
    while True:
        print('''
            Ingrese el número de la operación que desea 
            ejecutar:
            1 - Añadir un alumno a la lista.
            2 - Ver la lista de alumnos.
            3 - Salir
        ''')
        opcion = input("Ingrese la opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del alumno: ")
            cantidad_cursos = int(input("Ingrese la cantidad de cursos del alumno: "))
            alumnos.append(f"{nombre} - {cantidad_cursos} cursos")
            print(f"{nombre} se ha agregado correctamente")
        elif opcion == "2":
            print("Lista de alumnos:")
            for alumno in alumnos:
                print(alumno)
        elif opcion == "3":
            print("Gracias por usar el programa")
            break
        else:
            print("La opcion ingresada no es válida")
else:
    print("Credenciales erroneas")