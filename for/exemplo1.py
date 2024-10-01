import os

os.system('cls')

# for e in range (0,100, 5):  - nese caso, o 5 significa o salto, ou seja: exibe os número de 0 até 100 (exclusive), pulando de 5 em 5
#     print(e)

# for i in 'python':
#     print(i)


# inicio = int(input('Valor: '))
# fim = int(input("Valor final: "))

# for e in range(inicio, fim+1):
#     print(e)


s = 0
for e in range(5):
    n = int(input("Valor: "))
    s = s + n
    # print(e)

print (f"O valor total é {s}")