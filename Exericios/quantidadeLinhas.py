# Quantidade de linhas do arquivo personagens.txt


quantidadeLinhas = open("personagens.txt", "r")

contador = 0

for linha in quantidadeLinhas:
    contador += 1
    print(f"Linha {contador}: {repr(linha)}")

print("Total:", contador)

quantidadeLinhas.close()