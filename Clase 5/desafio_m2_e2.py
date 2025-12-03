# Copyright 2025 Manuel
rol = input("¿Cual es tu rol?")

if rol == "admin" or rol == "profesor":
    contrasena = input("Ingresa tu contraseña: ")
    if contrasena == "1234":
        nombre = input("Ingresa tu nombre: ")
        if nombre != "":
            print("Hola", nombre,"!")
        else: 
            print ("Nombre vacio")
    else: 
        print("Contraseña invalida")
else: 
    print("rol incorrecto")