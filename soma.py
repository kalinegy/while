soma=0
num=int(input("Digite números positivos(0 para parar):"))

while num != 0:
    if num > 0:
        soma+= num
    else:
        print("Número negativo, tente novamente")
    num= int(input("Digite outro número(0 para parar):"))
print(f"A soma é {soma}")

#não soma
