# Quantidade de caracteres de Video Game 

linhas = open("personagens.txt", "r")

for linha in linhas:
    conteudo = linhas.read()

print (len(conteudo))


linhas.close()