valores = []

while True:
    numero = nt(input("Digite um numero (999 para interromper): )"))
        if numero == 999:
            break
        
valores.append(numero)

valores.sort()
pint("Valores em ordem : ", valores)