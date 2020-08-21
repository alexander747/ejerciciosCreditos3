n = 0
aprobado = 0
suspendido = 0

while n < 15:
    nota = int(input("ingrese la nota"))
    if nota >= 3:
        aprobado += int(1)
    else:
        suspendido += int(1)
    n += int(1)

print("la cantidad de usuarios suspendidos es "+str(suspendido))
print("la cantidad de usuarios aprobados es "+str(aprobado))
