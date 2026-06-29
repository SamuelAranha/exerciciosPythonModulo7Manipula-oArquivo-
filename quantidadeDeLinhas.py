#Uma instituição deseja saber quantos registros existem em um arquivo de texto. 

#Desenvolva um programa que leia um arquivo e informe a quantidade de linhas armazenadas. 

quantidadeLinhas = open("alunos.txt", "r")

contador = 0

for linha in quantidadeLinhas:
    contador += 1
    print(f"Linha {contador}: {repr(linha)}")

print("Total:", contador)