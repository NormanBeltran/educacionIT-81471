# Continue 
# Break

n = 1

while n <= 10:
    
    n += 1
    if n%2 == 0:  # Si el nro es par
        continue

    print(n)    
    if n == 7:
        break

print("Fin de Programa")    