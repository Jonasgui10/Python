import random

aluno1=input(' Qual o nome do aluno?')
aluno2=input('Qual o nome do aluno?')
aluno3=input('Qual o nome do aluno?')
aluno4=input('Qual o nome do aluno?')
lista=[aluno1,aluno2,aluno3,aluno4]
random.shuffle(lista)
print(lista)