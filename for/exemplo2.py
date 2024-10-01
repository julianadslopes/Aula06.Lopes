import os

os.system ("cls")

previsoes =["Ensolarado", "Nublado", "Chuvoso", "Tempestade", "Ensolarado"]

for i in previsoes:
    if i == "Ensolarado":
        print ("Aproveite para passear!")
    else:
        print ("Não esqueça o guarda-chuva!")


# previsoes =["Ensolarado", "Nublado", "Chuvoso", "Tempestade", "Ensolarado"]
# for i in previsoes:
#     match i:
#         case "Ensolarado":
#             print ("Aproveite para passear!")
        
#         case _:    
#             print ("Não esqueça o guarda-chuva!")