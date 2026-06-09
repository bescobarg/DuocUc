
print("calculadora")
n1 = int(input("ingresa un numero"))
n2 = int(input("ingresa otro numero"))

while True:
    print("menu de opciones")
    print("opcion 1 sumar")
    print("opcion 2 restar")
    print("opcion 3 dividir")
    print("opcion 4 multiplicar")
    opc = int(input("ingresa una opcion"))

    if opc == 1:
        print("la suma es: ", n1 + n2)
        break
    if opc == 2:
        print("la resta es: ", n1 - n2)
        break
    if opc == 3:
        print("la division es: ", n1 / n2)
        break
    if opc == 4:
        print("la multiplicacion es: ", n1 * n2)
        break


