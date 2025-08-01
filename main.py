#Verificador de triangulos

lado1 = float(input("INGRESE EL LADO A DEL TRIANGULO: "))
lado2 = float(input("INGRESE EL LADO B DEL TRIANGULO: "))
lado3 = float(input("INGRESE EL LADO C DEL TRIANGULO: "))

if (lado1 == lado2 == lado3):
    print("EL TRIANGULO ES EQUILATERO")

elif (lado1 != lado2 != lado3):
    print("EL TRIANGULO ES ESCALENO")

else:
    print("EL TRIANGULO ES ISOSCELES")