# Copyright 2025 Lucas Dearma

nota = int(input("Coloca tu nota: "))

if nota == 10:
    print('Excelente')
elif 7 <= nota <=9:
    print('Muy bien')
elif 4 <= nota <= 6:
    print('Bien')
elif 0 <= nota <= 3:
    print('Mal')    
else:
    print(" La nota ingresada no es válida ")