#imprimir números primos entre 1 y 20
for num in range(2, 21):
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num)

