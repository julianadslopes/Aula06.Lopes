# Verificação de senha

# senha = "54321"
# leitura = " "

# while leitura != senha:
#     leitura = input("Digite a senha: ")
#     if leitura == senha:
#         print ("Acesso liberado")
#     else:
#         print ("Senha incorreta. Tente novamente")    

#-------------------exemplo-------------------

# Contagem regressiva usando while
# contador = 10
# while contador != 0:
#     print(contador)
#     contador -= 1   #condição de parada

#-------------------exemplo2-------------------

# s = 0
# c = 1

# while c < 4:
#     n = int (input("Informe um número: "))
#     s += n
#     c += 1
# print (f" O total é {s}")    

#-------------------exemplo3-------------------

# n = ""
# resposta = "S"
# while resposta != "N":
#     n = input ("Informe um texto: ")
#     resposta = input("Quer continuar S/N? ") [0].upper()

# print (n)    

#-------------------exemplo4-------------------

n = s = 0
while True:
    n = int(input("Número: "))
    if n == 999:
        break
    s = s + n
print(s)        