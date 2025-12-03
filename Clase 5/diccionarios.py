"""
Diccionarios

Mutables
No es ordenado
Elementos Clave-Valor / claves no se modifican / los valores si
Se pueden repetir solo los valores

"""

paises = { 
           "Argentina": "Buenos Aires", 
           "Chile": "Santiago",
           "Peru": "Lima",
           "Colombia": "Bogota",
           "Ecuador": "Quito",
           "Uruguay": "Montevideo",
           "Paraguay": "Asuncion"
}

print(paises["Argentina"])

# Agregar un elemento
paises["Venezuela"] = "Caracas"

# Modificar un elemento
paises["Chile"] = "Santiago de Chile"

# Eliminar un elemento
del paises["Peru"]

for p in paises:
    if p == "Colombia":
        print("La capital de", p, "es", paises[p], "fecha de independencia es el 20 de julio de 1810")
    else:
        print("La capital de", p, "es", paises[p])        

if "Paraguay" in paises:
    print("Paraguay se encuentra en el diccionario")