# Observando a quantidade de palavras

quantidadePalavras = open("personagens.txt", "r")

conteudo = quantidadePalavras.read()

print(len(conteudo.split()))

quantidadePalavras.close()