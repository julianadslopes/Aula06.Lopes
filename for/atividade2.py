import os

os.system('cls')
# Contagem regressiva de 10 até 0

# for i in range (10, 0, -1):
#     print (i)

# Pergunte um número n para o usuário e exiba todos os seus divisores

n = int(input("Digite um número: "))
divisores =[]

for i in range (1, n+1):
    if n % i == 0:
        divisores.append(i)
print(divisores)        