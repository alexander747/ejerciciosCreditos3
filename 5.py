n1 = int(input("ingrese el primer valor"))
n2 = int(input("ingrese el segundo valor"))

for n1 in range(n1, n2+1):
    print(str(n1))
    n1 += int(n1)
