#Fibonacci 10 términos
a, b = 0, 1
i = 0
while i < 10:
    print(a, end=" ")
    a, b = b, a+b
    i += 1
print()

