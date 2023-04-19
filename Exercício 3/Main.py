#Aluno: Pedro Wilson Rodrigues de Lima.
#Nº de Matrícula: 2020267
#Data: 19/04/2023


#Exercício de implentação de um programa em Python que multiplica os elementos de um vetor de tamanho 1000:

import numpy as np

def multiply(v, scalar):
    v *= scalar

v = np.arange(1000)

subvecs = np.reshape(v, (10, 100))

for i in range(10):
    multiply(subvecs[i], 2)

v = np.reshape(subvecs, 1000)

print(v)
