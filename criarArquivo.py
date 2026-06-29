#Uma escola deseja armazenar os nomes dos alunos em um arquivo de texto para consulta futura. 

#Desenvolva um programa que crie um arquivo chamado alunos.txt e grave cinco nomes informados pelo usuário. 

alunos = open("alunos.txt", "w")

for x in range(5): 
    nome = input("Digite seu nome: ")
    alunos.write(nome+'\n')


alunos.close()
