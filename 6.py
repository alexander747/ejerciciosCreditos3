n = int(1)
d = int(1)
for n in range(1, 11):
    print("TABLA DEL "+str(n))
    for d in range(1, 11):
        m = n*d
        print(str(n)+" * " + str(d)+" = "+str(m))
