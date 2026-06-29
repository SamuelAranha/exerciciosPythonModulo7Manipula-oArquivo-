
# Desenvolva um programa que leia e exiba todo o conteúdo do arquivo alunos.txt. 

alunosLer = open("alunos.txt", "r")

for linha in alunosLer:
    print(linha.strip())

alunosLer.close()