#1. Realiza un programa que permita obtener la media de 3 números.  	
l = 1 + 6 + 5
med = l/3
print med
#2. Realiza una función que permita obtener el volumen de una esfera.
import math

radio_esfera = float(input("ingresa el radio de la esfera:"))
3

un = radio_esfera **3
pi=(math.pi * 4)/3

vol = pi * un 

print ("el volumen es:", vol)
n = [12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
print (n[1:20:2])

#4. Realiza una función que permita obtener el máximo de 3 números.
n1= float(input("ingrese le primer dato"))
n2= float(input("ingrese le segundo dato"))
n3= float(input("ingrese le tercer dato"))

print( n1, n2, n3)


if n2< n1 >n3:
        print(n1)
if n1< n2 >n3:
        print("el mayor es el primer numero :",n2)
if n1< n3 >n2:
        print("el mayor es el primer numero :",n3)

# 5 rotar una lista
# 6 Realiza un programa que permita generar un intervalo de la suma de los cubos de los primeros n números. Ejemplo suma = 1 + 8 + 27 + n
def intervaloSuma(x):      
        vacio=[(conta**3) for conta in range(1,x+1)]        
        print vacio
        return sum(vacio)
#7. Realiza un programa que permita generar un intervalo de los cuadrados de n números mayores a 100.
sumMayor n=[x^2 | x <- [1..n], x^2>100]
def intervaloMax(x):
           vacio=[(conta**2) for conta in range(1,x+1)]        
        num=1
        while num<len(vacio):
                if vacio[num]>100:
                        print vacio[num]
                num+=1
#8. Realiza un programa que permita generar un intervalo de n numeros entre 20 y 60
def interva20(x):
        cont=1
        while cont<=x:
                if cont>=20 and cont<=60:
                        print cont
                cont+=1

#9. Realiza un programa que solicite dos argumentos de tipo Double para calcular la hipotenusa de un triángulo rectángulo y retorne un valor de tipo Double.
import math
a = float(input("ingrese l primer dato: ") ) 
3
b = float(input("ingrese 2 primer dato: "))
4
print "la hipotnusa es: " + str(math.sqrt((a*a)+(b*b)))

#10. Crear un programa que por medio de recursión calcule la suma de los cuadrados de n números.




