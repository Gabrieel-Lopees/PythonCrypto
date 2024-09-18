'''Primeira aula pratica de python em cryptografia 

x = "pyhton"
y = "é"
z = "legal"

username = input ("Seu nome: ")
print ("Olá, ", username)

print (x, y, z) '''

'''print("Olá Mundo")'''

'''x = int(input ("Variavel um:"))
y = int(input ("Variavel dois: "))

if x > y:
    print("X é maior que Y!")
elif y == x: 
    print("São iguais!")
    
else:
    print("Y é maior que X!")'''
    
x = int(input ("Variavel X:"))
y = int(input ("Variavel Y: "))
z = int(input ("Variavel Z: "))

#verificar se é Z
if x > z and y > z:
    print("Z é a menor")
#verificar se é X
elif z > x and y > x: 
    print("X é a menor")
#verificar se é Y
else:
    print("Y é a menor")