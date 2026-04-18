#1. Básico
for i in range(101):
    print(i)
#2. Múltiples de 2
for i in range(2, 501, 2):
    print(i)
#3. Contando Vanilla Ice
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)
#4. Wow. Número gigante a la vista
suma = sum(i for i in range(0, 500001, 2))
print(suma)
#5.Regrésame al 3
for i in range(2024, 0, -3):
    print(i)
#6.Contador dinámico
numFinal = 10
multiplo = 2
for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)
