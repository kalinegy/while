
numI= int(input("Digite o número inicial:"))
numF= int(input("Digite o número final:"))
if numI <= numF:
    while numI <= numF:
        print(numI)
        numI+=1
else:
    while numI >= numF:
        print(numI)
        numI -= 1