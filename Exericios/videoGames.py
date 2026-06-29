# Criando um arquivo txt com o nome de protagonistas de jogos 

protagonistas = open("personagens.txt", "w")

for linhas in range(6):
    protagonista = input("Digite um nome: ")
    protagonistas.write(protagonista+"\n")
    
protagonistas.close()