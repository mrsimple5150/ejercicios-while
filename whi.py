w = input("type a word without ñ: ")
z = w.count("ñ")

while z >= 1:
    print("wrong")
    w = input("try again: ")
    z = w.count("ñ")
    if not z != 0:#si z no es diferente a 0 entonces es igual
        print("right")
print("fin")

#if not z >= 1: aqui tiene que ser cero / no puede ser ni mayor ni igual
#if z == 0: aqui zeta tiene que ser 0

a = input("ingresa una palabra con 'dos' letras 'a': ")
a = a.lower()
b = a.count("a")

if b == 2:
    print("lo lograste a la primera")

while b <= 1 or b >= 3:
    
    print("incorrecto")
    a = input("intenta otra vez: ")
    b = a.count("a")
    if not b != 2:
        print("lo lograste despues de varios intentos")

print("fin")

#if b == 2:
#if not b != 2:

string = "stocking" #= 8
stint = len(string) # = 8

key = input("keyword must have more than 8 letters: ")
stint2 = len(key)

while stint2 > stint:
    key = input("do it again: ")
    stint2 = len(key)
else:
    print("wrong")

#Mientras la palabra sea mayor a 8 el programa seguira.
#Si colocas 8 o menos se acabara e imprimira wrong