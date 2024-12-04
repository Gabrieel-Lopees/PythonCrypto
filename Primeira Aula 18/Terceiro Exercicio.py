x = int(input ("Variavel X: "))
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