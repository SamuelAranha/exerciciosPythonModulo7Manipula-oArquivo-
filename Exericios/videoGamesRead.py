#Ler os dados que foram escritos em 'videoGames'

listaPersonagens = open("personagens.txt", "r")

for linhas in listaPersonagens:
    print(linhas.strip())
    
listaPersonagens.close()
