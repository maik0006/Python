print(" Seleccione la operacion que desea realizar")
a=int(input("1)sumar 2)restar 3)multiplicar 4)dividir 5)potencia 6)raiz 7)factorial 8)salir: ") )

while a!=8:
    if a == 1:
        num1=int(input("Ingrese un numero: "))
        num2=int(input("Ingrese un numero: "))

        suma=num1+num2
        print("El resultado de la suma es: ",suma)
        print("¿Quiere realizar otra operacion")
        a=int(input("1)sumar 2)restar 3)multiplicar 4)dividir 5)potencia 6)raiz 7)factorial 8)salir: ") )

    elif a == 2: 
        num1=int(input("Ingrese un numero: "))
        num2=int(input("Ingrese un numero: "))

        resta=num1-num2
        print("El resultado de la resta es: ",resta)
        print("¿Quiere realizar otra operacion")
        a=int(input("1)sumar 2)restar 3)multiplicar 4)dividir 5)potencia 6)raiz 7)factorial 8)salir: ") )

    elif a == 3: 
        num1=int(input("Ingrese un numero: "))
        num2=int(input("Ingrese un numero: "))

        multiplicacion=num1*num2
        print("El resultado de la multiplicacion es: ",multiplicacion)
        print("¿Quiere realizar otra operacion")
        a=int(input("1)sumar 2)restar 3)multiplicar 4)dividir 5)potencia 6)raiz 7)factorial 8)salir: ") )

    elif a == 4: 
        num1=int(input("Ingrese un numero: "))
        num2=int(input("Ingrese un numero: "))

        division=num1/num2
        print("El resultado de la division es: ",division)
        print("¿Quiere realizar otra operacion")
        a=int(input("1)sumar 2)restar 3)multiplicar 4)dividir 5)potencia 6)raiz 7)factorial 8)salir: ") )

    elif a == 5: 
        num1=int(input("Ingrese un numero : "))
        num2=int(input("Ingrese el numero al que lo quiere elevar: "))

        potencia=(num1**num2)
        print("El resultado de la potenciacion es: ",potencia)
        print("¿Quiere realizar otra operacion")
        a=int(input("1)sumar 2)restar 3)multiplicar 4)dividir 5)potencia 6)raiz 7)factorial 8)salir: ") )

    elif a == 6: 
        import math
        num1=int(input("Ingrese un numero : "))
        num2=int(input("Ingrese la  el numero de la raiz que quieres obtener: "))

        raiz=(num1**(1/num2))
        print("El resultado de la raiz es: ",raiz)
        print("¿Quiere realizar otra operacion")
        a=int(input("1)sumar 2)restar 3)multiplicar 4)dividir 5)potencia 6)raiz 7)factorial 8)salir: ") )

    elif a == 7: 
        import math
        num1=int(input("Ingrese un numero : "))
 
        factorizacion=(math.factorial(num1))
        print("El resultado de la factorizacion es: ",factorizacion)
        print("¿Quiere realizar otra operacion")
        a=int(input("1)sumar 2)restar 3)multiplicar 4)dividir 5)potencia 6)raiz 7)factorial 8)salir: ") )

print("Gracias por utilizar este sistema")




